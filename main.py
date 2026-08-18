import config
import database as db
from bot import build_application, setup_scheduler


def main():
    # Database initialize
    db.init_db()

    # Bot build
    application = build_application()
    
    # Scheduler setup (auto-expiry)
    setup_scheduler(application)

    print("🚀 Bot chalu ho gaya! (3rd Party Payment Only)")
    print("✅ Commands:")
    print("   User: /start, /buy")
    print("   Owner: /addgroup, /addplan, /grant, /extend, /revoke, /listsubs, /admin")
    print("   Owner: /listgroups, /listplans")
    
    application.run_polling()


if __name__ == "__main__":
    main()
