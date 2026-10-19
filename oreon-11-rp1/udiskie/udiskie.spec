%global source0_hash 316b2feba0e415429e5632b5367c9b6366cb8a90cf919cd8a1053bbb26492bb3
Name:           udiskie
Version:        2.7.0
Release:        1%{?dist}
Summary:        Removable disk auto-mounter
License:        MIT
URL:            https://github.com/coldfix/udiskie
Source0:        https://files.pythonhosted.org/packages/source/u/udiskie/udiskie-%{version}.tar.gz
Source1:        50-udiskie.rules
BuildArch:      noarch
Requires:       python3-%{name} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       polkit
Recommends:     libnotify
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-udiskie = %{version}-%{release}
# /oreon:deps
%description
%{name} is a front-end for UDisks written in python. Its main purpose is
automatically mounting removable media, such as CDs or flash drives. It has
optional mount notifications, a GTK tray icon and user level CLIs for manual
mounting and unmounting operations.

%package -n python3-%{name}
Summary:        Removable disk auto-mounter
%description -n python3-%{name}
%{name} is a front-end for UDisks written in python. This package provides the
python 3 modules used by the %{name} binaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%make_build -C doc
%install
%pyproject_install
install -p -m644 -Dt ${RPM_BUILD_ROOT}%{_sysconfdir}/polkit-1/rules.d %{SOURCE1}
install -p -m644 -Dt ${RPM_BUILD_ROOT}%{_mandir}/man8 doc/%{name}.8
for other in %{name}-mount %{name}-umount %{name}-info; do
    printf '.so man8/%%s.8\n' %{name} > ${RPM_BUILD_ROOT}%{_mandir}/man8/"${other}.8"
done
%find_lang %{name}
%oreon_autofiles main usr/lib/python3*/site-packages/udiskie* usr/lib64/python3*/site-packages/udiskie* usr/bin/*

%check

%{python3} -m unittest test.test_match
%files
%files -n python3-udiskie -f %{oreon_filedir}/python3-udiskie.list

%changelog

%autochangelog
