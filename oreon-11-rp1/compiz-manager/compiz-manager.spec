%global source0_hash cdb6fdd379c80902b8555e5ee6ab148e762e63d17c384825c07d5798e8df19a5

Name:           compiz-manager
Version:        0.7.0
Release:        26%{?dist}
Summary:        A wrapper script to start compiz with proper options

License:        GPL-2.0-or-later
URL:            https://github.com/raveit65/%{name}/
Source0:        https://github.com/raveit65/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch

Requires:       compiz
Requires:       xdpyinfo
Requires:       pciutils
Requires:       glx-utils
Requires:       libcompizconfig

# Already fixed in upstream git
Patch0:         compiz-manager-0.7.0-xfwm4-fix.patch

%description
This script will detect what options we need to pass to compiz to get it
started, and start a default plugin and possibly window decorator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
#no build needed

%install
mkdir -p %{buildroot}/%{_bindir}/
cp -p %{name} %{buildroot}/%{_bindir}/

%files
%doc COPYING README.md
%{_bindir}/%{name}

%changelog
%autochangelog
