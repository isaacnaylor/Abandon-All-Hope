import minecraft
EntityType = minecraft.gateway.jvm.org.bukkit.entity.EntityType
System = minecraft.gateway.jvm.java.lang.System
Material = minecraft.gateway.jvm.org.bukkit.Material
GameMode = minecraft.gateway.jvm.org.bukkit.GameMode

print = System.out.println
print('Hello Iron Man!')

def on_projectile_hit(event):
    projectile = event.getEntity()
    if projectile.getType().toString() == "SNOWBALL":
        projectile.getWorld().createExplosion(projectile.getLocation(), 8.0, True, True)

def on_inventory_click(event):
    print(f"action: {event.getAction().toString()}")
    print(f"click: {event.getClick().toString()}")
    print(f"slotType: {event.getSlotType().toString()}")
    print(f"slot: {event.getSlot()}")
    inventory = event.getInventory()
    print(f"inventory: {inventory.getType().toString()}")

    slot = event.getSlot()
    slot_type = event.getSlotType().toString()

    cursor_item = event.getCursor()
    if cursor_item:
        cursor_item_name = cursor_item.getType().toString()
    else:
        cursor_item_name = "*nothing*"

    if slot == 36 and slot_type == "ARMOR" and cursor_item_name == "IRON_BOOTS":
        print("*** PUTTING ON iron boots")

        player = event.getClickedInventory().getHolder()
        player.setAllowFlight(True)
        player.setMaxHealth(100.0)
        player.setHealth(100.0)
        player.getWorld().strikeLightningEffect(player.getLocation())

    inv_item = event.getCurrentItem()
    if inv_item:
        inv_item_name = inv_item.getType().toString()
    else:
        inv_item_name = "*nothing*"

    if slot == 36 and slot_type == "ARMOR" and inv_item_name == "IRON_BOOTS":
        print("*** TAKING OFF iron boots")

        player = event.getClickedInventory().getHolder()
        if player.getGameMode().toString() != "CREATIVE":
            player.setAllowFlight(False)
        player.setMaxHealth(20.0)

    #all_iron_helmets = inventory.all(Material.IRON_HELMET)
    #for key in all_iron_helmets.keys():
    #    System.out.println(f"iron helmet found under key: {key}")

    print()

def on_player_join(event):
    print(event.toString())

def on_player_game_mode_change(event):
    player = event.getPlayer()
    inventory = player.getInventory()
    inv_item = inventory.getItem(36)
    if inv_item and inv_item.getType().toString() == "IRON_BOOTS":
        player.setAllowFlight(True)
        player.setFlying(True)
        player.setMaxHealth(100.0)
    else:
        player.setAllowFlight(False)
        player.setMaxHealth(20.0)

minecraft.on_event("InventoryClickEvent", on_inventory_click)
minecraft.on_event("PlayerJoinEvent", on_player_join)
minecraft.on_event("PlayerGameModeChangeEvent", on_player_game_mode_change)
minecraft.on_event("ProjectileHitEvent", on_projectile_hit)

