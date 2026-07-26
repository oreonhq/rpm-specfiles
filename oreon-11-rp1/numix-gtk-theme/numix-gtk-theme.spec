%global source0_hash 2b997ad3eee0b802d0dd49dd772127fd3c337cca32d8863efd4897928e38879a

Name:		numix-gtk-theme
Version:	2.6.7
Release:	18%{?dist}
Summary:	Numix Gtk Theme

Source:		https://github.com/numixproject/numix-gtk-theme/archive/%{version}.tar.gz#/numix-gtk-theme-%{version}.tar.gz

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/numixproject/numix-gtk-theme

BuildArch:	noarch

BuildRequires: make
BuildRequires:	rubygem-sass
BuildRequires:	gdk-pixbuf2-devel
Requires:	filesystem
Requires:	gtk-murrine-engine

%description
Numix is a modern flat theme with a combination of light and dark elements.
It supports Gnome, Unity, XFCE and Openbox.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
find -type f -executable -exec chmod -x {} \;

%install
chmod +x scripts/utils.sh
%make_install

%files
%license LICENSE
%doc README.md
%doc CREDITS
%{_datadir}/themes/Numix

# This is to clean up directories before links created
# See https://bugzilla.redhat.com/show_bug.cgi?id=1379883
# See https://fedoraproject.org/wiki/Packaging:Directory_Replacement
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

%changelog
%autochangelog
