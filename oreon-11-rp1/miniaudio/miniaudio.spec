%global source0_hash 6afb5c231613d2fab4f1c668b7243ff9a7d6d78a7f5a2692c133f026fe508506

%global debug_package %{nil}

Name:           miniaudio
Version:        0.11.21
Release:        5%{?dist}
Summary:        Audio playback and capture library

License:        MIT-0
URL:            https://miniaud.io/
Source0:        https://github.com/mackron/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%package devel
Summary: %summary
Provides:       miniaudio-static = %{version}-%{release}
BuildArch:      noarch

%description
%summary

%description devel
%summary

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build

%check
# The package does include tests but they are interactive so we cannot use them

%install
mkdir -p %{buildroot}%{_includedir}
install -p %{name}.h %{buildroot}%{_includedir}/

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}.h

%changelog
%autochangelog
