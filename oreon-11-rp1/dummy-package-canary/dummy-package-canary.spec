%global source0_hash none

Name:           dummy-package-canary
Version:        2
Release:        %autorelease
Summary:        Dummy package to exercise the packaging stack

License:        CC-PDDC

BuildArch:      noarch

Provides:       canary = %{version}-%{release}

%description
This a dummy canary package to exercise the packaging stack and make sure it
actually works as expected (e.g. by removing and installing this package as
part of a configuration management flow).

%prep
echo %{name} > %{name}

%build

%install
install -Dpm0644 -t %{buildroot}%{_datadir}/%{name} %{name}

%files
%{_datadir}/%{name}

%changelog
%autochangelog
