%global source0_hash b77041324f0109f77161ee43743fe04baa485866af8460d31e476ad3f7648fd5
%global debug_package %{nil}
%global pkgconfig_name xkeyboard-config-2
Summary:        X Keyboard Extension configuration data
Name:       xkeyboard-config
Version:    2.48
Release:        1%{?dist}
License:    HPND AND HPND-sell-variant AND X11 AND X11-distribute-modifications-variant AND MIT AND MIT-open-group AND xkeyboard-config-Zinoviev
URL:        http://www.freedesktop.org/wiki/Software/XKeyboardConfig
%if 0%{?gitdate}
Source0:        https://www.x.org/archive/individual/data/%{name}/%{name}-%{version}.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
%endif
BuildArch:  noarch
# oreon:deps
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  git-core
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  xkbcomp
# /oreon:deps
%description
This package contains configuration data used by the X Keyboard Extension (XKB),
which allows selection of keyboard layouts when using a graphical interface.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig
%description devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dcompat-rules=true -Dxorg-rules-symlinks=true
%meson_build
%install
%meson_install
rm $RPM_BUILD_ROOT%{_datadir}/X11/xkb
ln -srf $RPM_BUILD_ROOT%{_datadir}/%{pkgconfig_name} $RPM_BUILD_ROOT%{_datadir}/X11/xkb
%find_lang %{pkgconfig_name}
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%pretrans -p <lua>

-- Define the path to directory being replaced below.
-- DO NOT add a trailing slash at the end.
local path = "%{_datadir}/X11/xkb"
local st = posix.stat(path)
if st and st.type == "directory" then
  local target = path .. ".rpmmoved"
  local suffix = 1
  while posix.stat(target) do
    suffix = suffix + 1
    target = path .. ".rpmmoved" .. suffix
  end
  os.rename(path, target)
end
%files -f %{oreon_filedir}/main.list
%files -n xkeyboard-config-devel -f %{oreon_filedir}/xkeyboard-config-devel.list

%changelog

%autochangelog
