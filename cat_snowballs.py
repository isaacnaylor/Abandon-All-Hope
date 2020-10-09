import minecraft

def on_projectile_hit(event):
    projectile = event.getEntity()
    if projectile.getType().toString() == "SNOWBALL":
        projectile.getWorld().spawnEntity(projectile.getLocation(), minecraft.gateway.jvm.org.bukkit.entity.EntityType.CAT)
        projectile.getWorld().strikeLightningEffect(projectile.getLocation())

minecraft.on_event("ProjectileHitEvent", on_projectile_hit)