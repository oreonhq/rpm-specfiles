%global source0_hash ac2f9015137935279eac671f94f89eb00584f940f5dc49462a0c4ee692ba1bd9

%global pypi_name isoduration

Name:           python-%{pypi_name}
Version:        20.11.0
Release:        16%{?dist}
Summary:        Operations with ISO 8601 durations

License:        ISC
URL:            https://github.com/bolsote/isoduration
Source0:        %{url}/releases/download/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
ISO 8601 is most commonly known as a way to exchange datetimes in textual
format. A lesser known aspect of the standard is the representation of
durations. They have a shape similar to this: P3Y6M4DT12H30M5S

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
ISO 8601 is most commonly known as a way to exchange datetimes in textual
format. A lesser known aspect of the standard is the representation of
durations. They have a shape similar to this: P3Y6M4DT12H30M5S

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# upstream does not bundle any tests in released tarball
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
