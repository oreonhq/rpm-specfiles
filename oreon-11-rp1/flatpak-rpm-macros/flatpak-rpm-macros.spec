%global source0_hash none
Name:           flatpak-rpm-macros
Version:        44
Release:        1%{?dist}
Summary:        Macros for building RPMS for flatpaks
Source0:        macros.flatpak.in
Source1:        distutils.cfg
Source2:        flatpak.xml
Source3:        fontconfig-flatpak.prov
License:        MIT
# oreon:deps
BuildRequires:  python3-devel
# /oreon:deps
%description
The macros in this package set up the RPM build environment so built
applications install in /app rather than /usr. This package is meant
only for installation in buildroots when rebuilding RPMS to package
in Flatpaks.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%build

sed -e 's|__LIB__|%{_lib}|g' \
    %{SOURCE0} > macros.flatpak
%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
install -t $RPM_BUILD_ROOT%{_sysconfdir}/rpm -p -m 644 macros.flatpak
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{python3_version}/distutils/
install -t $RPM_BUILD_ROOT%{_libdir}/python%{python3_version}/distutils/ %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/xmvn/config.d
install -t $RPM_BUILD_ROOT%{_sysconfdir}/xdg/xmvn/config.d -m 644 %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}
install -t $RPM_BUILD_ROOT%{_rpmconfigdir} -m 755 %{SOURCE3}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 44-1
- Prepare for Oreon 11 (RP1)
