%global source0_hash 2b997ad3eee0b802d0dd49dd772127fd3c337cca32d8863efd4897928e38879a
Name:		numix-gtk-theme
Version:	2.6.7
Release:        1%{?dist}
Summary:        Numix Gtk Theme
Source0:        https://github.com/numixproject/numix-gtk-theme/archive/%{version}.tar.gz#/numix-gtk-theme-%{version}.tar.gz
License:	GPL-3.0-only
URL:		https://github.com/numixproject/numix-gtk-theme
BuildArch:	noarch
Requires:	filesystem
Requires:	gtk-murrine-engine
# oreon:deps
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  make
BuildRequires:  rubygem-sass
# /oreon:deps
%description
Numix is a modern flat theme with a combination of light and dark elements.
It supports Gnome, Unity, XFCE and Openbox.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

find -type f -executable -exec chmod -x {} \;
%install
chmod +x scripts/utils.sh
%make_install
%oreon_autofiles main

%pretrans -p <lua>

directories = {
  "/usr/share/themes/Numix/gtk-3.0/assets",
  "/usr/share/themes/Numix/gtk-3.2/assets"
}
for i,path in ipairs(directories) do
  st = posix.stat(path)
  if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
      suffix = 0
      while not status do
				suffix = suffix + 1
				status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
      end
      os.rename(path, path .. ".rpmmoved")
    end
  end
end
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
