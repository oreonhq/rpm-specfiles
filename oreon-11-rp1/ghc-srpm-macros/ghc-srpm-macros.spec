%global source0_hash none

%global macros_dir %{_rpmconfigdir}/macros.d

%global macrosfile macros.ghc-srpm

Name:           ghc-srpm-macros
Version:        1.10
Release:        %autorelease
Summary:        RPM macros for building Haskell source packages

License:        GPL-2.0-or-later
URL:            https://src.fedoraproject.org/rpms/ghc-srpm-macros
BuildArch:      noarch

Source0:        %{macrosfile}

%description
Macros used when generating Haskell source RPM packages.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{nil}


%build
echo no build stage needed


%install
install -p -D -m 0644 %{SOURCE0} %{buildroot}/%{macros_dir}/%{macrosfile}


%files
%{macros_dir}/%{macrosfile}


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10-1
- Import
