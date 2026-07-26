%global source0_hash e3f64feaeb9c1e6bcf55fb432b5000db300b6c83a150de05da5594f2ca3faa05

%bcond_without tests

%global pretty_name openant
%global extract_name ant

%global _description %{expand:
A python library to download and upload files from ANT-FS 
compliant devices (Garmin products).Any compliant ANT-FS 
device should in theory work, but those specific devices 
have been reported as working: Garmin Forerunner 60,
Garmin Forerunner 405CX, Garmin Forerunner 310XT, Garmin 
Forerunner 610, Garmin Forerunner 910XT, Garmin FR70, 
Garmin Swim}

Name:           python-%{pretty_name}
Version:        1.3.3
Release:        6%{?dist}
Summary:        A python library to communicate with ANT-FS compliant devices

License:        MIT
URL:            https://github.com/Tigge/openant
Source0:        %{url}/archive/v%{version}/%{pretty_name}-%{version}.tar.gz
Source2:        ant-usb-sticks.rules

BuildArch:      noarch

# For udev-rules	
BuildRequires:  systemd

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist pyusb}
BuildRequires:  %{py3_dist pytest}

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}

%description -n python3-%{pretty_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pretty_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%pyproject_install
%pyproject_save_files openant

%{!?_udevrulesdir: %global _udevrulesdir %{_sysconfdir}/udev/rules.d}

mkdir -pm 755 %{buildroot}/%{_udevrulesdir}	
install -pm 644 %{SOURCE2} %{buildroot}/%{_udevrulesdir}

%check
%{pytest}

%post
%udev_rules_update

%postun
%udev_rules_update

%files -n python3-%{pretty_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/openant
%config(noreplace) %{_udevrulesdir}/*

%changelog
%autochangelog
