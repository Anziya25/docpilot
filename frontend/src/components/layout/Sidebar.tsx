import {
  FileText,
  MessageSquare,
  LayoutDashboard,
  Settings,
  Database,
} from "lucide-react";

const menuItems = [
  {
    icon: LayoutDashboard,
    label: "Dashboard",
  },
  {
    icon: FileText,
    label: "Documents",
  },
  {
    icon: MessageSquare,
    label: "Chat",
  },
  {
    icon: Database,
    label: "Knowledge Base",
  },
  {
    icon: Settings,
    label: "Settings",
  },
];

export default function Sidebar() {
  return (
    <aside className="w-72 bg-slate-950 border-r border-slate-800 flex flex-col">

      {/* Logo */}
      <div className="px-6 py-8 border-b border-slate-800">

        <h1 className="text-3xl font-bold text-blue-500">
          🚀 DocPilot
        </h1>

        <p className="text-slate-400 text-sm mt-2">
          AI-powered Document Assistant
        </p>

      </div>

      {/* Navigation */}

      <nav className="flex-1 px-4 py-6">

        <div className="space-y-2">

          {menuItems.map((item) => {

            const Icon = item.icon;

            return (

              <button
                key={item.label}
                className="
                w-full
                flex
                items-center
                gap-4
                rounded-xl
                px-4
                py-3
                text-slate-300
                hover:bg-blue-600
                hover:text-white
                transition-all
                duration-200
                "
              >

                <Icon size={20} />

                <span>{item.label}</span>

              </button>

            );
          })}

        </div>

      </nav>

      {/* Footer */}

      <div className="border-t border-slate-800 p-5">

        <p className="text-xs text-slate-500">
          Version 1.0
        </p>

      </div>

    </aside>
  );
}