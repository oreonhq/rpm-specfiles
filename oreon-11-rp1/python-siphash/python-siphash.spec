%global source0_hash aee97fe95e09a2995819c058a5e4ac6d96661a898d7fe0ad55e3b72c9a31d461

%global pypi_name siphash

Name:           python-%{pypi_name}
Version:        0.0.1
Release:        23%{?dist}
Summary:        SipHash in Python

License:        MIT
URL:            http://github.com/majek/pysiphash
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
A Python implementation of SipHash-2-4, a fast short-input PRF with a 128-bit
key and 64-bit output.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A Python implementation of SipHash-2-4, a fast short-input PRF with a 128-bit
key and 64-bit output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md Changelog

%changelog
%autochangelog
