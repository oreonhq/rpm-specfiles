%global source0_hash dde474c2bce436396a9b9c56e5db608a1b37ddc554999792d3fadffb19cf7916

# For test builds, should be set to 0 for release builds.
%global alpha 0

Name:           flmsg
Version:        4.0.23
Release:        8%{?dist}
Summary:        Fast Light Message Amateur Radio Forms Manager

# Embedded mongoose is GPLv2
License:        GPL-3.0-or-later AND GPL-2.0-only
URL:            http://www.w1hkj.com/
%if %{alpha}
Source0:        http://www.w1hkj.com/alpha/%{name}/%{name}-%{version}.tar.gz
%else
Source0:        http://www.w1hkj.com/files/%{name}/%{name}-%{version}.tar.gz
%endif
Source100:      flmsg.appdata.xml

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++ make
BuildRequires:  fltk-devel >= 1.3.0
%if 0%{?fedora}
BuildRequires:  flxmlrpc-devel >= 1.0
BuildRequires:  libappstream-glib
%endif

# While mongoose does make official releases, it is also designed as a copylib
# The copy in flmsg is heavily modified and will not work with any upstream 
# version.
# https://github.com/cesanta/mongoose
Provides:       bundled(mongoose)

%description
flmsg is a editor / file management tool for ics213 forms which form the
basis for emergency communications data transfers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%if 0%{?fedora}
# Remove bundled xmlrpc library.
rm -rf src/xmlrpcpp
%endif

%build
%configure
%make_build

%install
%make_install

%if 0%{?fedora}
mkdir -p %{buildroot}%{_datadir}/metainfo
install -pm 0644 %{SOURCE100} %{buildroot}%{_datadir}/metainfo/
%endif

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%if 0%{?fedora}
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%endif

%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{?fedora:%{_datadir}/metainfo/*.xml}
%{_datadir}/pixmaps/%{name}.xpm

%changelog
%autochangelog
