%global source0_hash 72e582920ba25a646203e93c2d2331d87f03037a28894d6c7e99af00ee043257

Name:           surf
Version:        2.1
Release:        7%{?dist}
Summary:        Simple web browser
License:        MIT
URL:            http://surf.suckless.org/

Source0:        http://dl.suckless.org/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.svg

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.1)
BuildRequires:  desktop-file-utils

Requires:       st
Requires:       dmenu
# https://bugzilla.redhat.com/show_bug.cgi?id=841348
Requires:       xprop
# https://bugzilla.redhat.com/show_bug.cgi?id=884296
Requires:       xterm
Requires:       wget, curl
# Appdata file needed later.

%description
surf is a simple web browser based on WebKit/GTK+.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Adapt to Fedora FHS
# Also use correct webkit2gtk version
# Cf. https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version
sed \
  -e 's|/usr/local|%{_prefix}|g' \
  -e 's|$(PREFIX)/lib|$(PREFIX)/%{_lib}|g' \
  -e 's|webkit2gtk-4.0|webkit2gtk-4.1|g' \
  -e 's|webkit2gtk-web-extension-4.0|webkit2gtk-web-extension-4.1|g' \
  -i config.mk

sed -i 's!^\(\t\+\)@!\1!' Makefile

%build
%set_build_flags
%make_build

%install
%make_install INSTALL="install -p"

desktop-file-install %{S:1} --dir=%{buildroot}%{_datadir}/applications/

mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -pm0644 %{S:2} %{buildroot}%{_datadir}/pixmaps/

%files
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/webext-%{name}.so
%{_mandir}/man*/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg

%changelog
%autochangelog
