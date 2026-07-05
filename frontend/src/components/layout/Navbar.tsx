import { Bell, Moon, Search, UserCircle2 } from "lucide-react";

export default function Navbar() {
  return (
    <header className="h-20 border-b border-slate-800 bg-slate-950 flex items-center justify-between px-8">

      {/* Left */}

      <div>

        <h2 className="text-2xl font-bold text-white">
          Dashboard
        </h2>

        <p className="text-sm text-slate-400">
          Welcome back to DocPilot
        </p>

      </div>

      {/* Right */}

      <div className="flex items-center gap-4">

        {/* Search */}

        <div className="hidden md:flex items-center gap-2 rounded-xl bg-slate-900 px-4 py-2 border border-slate-800">

          <Search size={18} className="text-slate-400" />

          <input
            placeholder="Search documents..."
            className="bg-transparent outline-none text-sm text-white placeholder:text-slate-500 w-64"
          />

        </div>

        {/* Notification */}

        <button className="rounded-xl bg-slate-900 p-3 hover:bg-slate-800 transition">

          <Bell size={20} />

        </button>

        {/* Theme */}

        <button className="rounded-xl bg-slate-900 p-3 hover:bg-slate-800 transition">

          <Moon size={20} />

        </button>

        {/* Profile */}

        <button className="rounded-xl bg-blue-600 p-2">

          <UserCircle2 size={28} />

        </button>

      </div>

    </header>
  );
}