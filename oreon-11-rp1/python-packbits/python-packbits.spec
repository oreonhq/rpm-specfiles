%global source0_hash 34a3c8d41584069718eae52c56d449ba28d49b52263b032ec46934f789d80121

Name:           python-packbits
Version:        0.6
Release:        %autorelease
Summary:        PackBits encoder/decoder

License:        MIT
URL:            https://github.com/kmike/packbits
# PyPI tarball doesn't include tests
Source:         %{url}/archive/%{version}/packbits-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This module implements a PackBits encoder/decoder for Python. PackBits encoding
is used in PSD and TIFF files.}

%description %_description

%package -n     python3-packbits
Summary:        %{summary}

%description -n python3-packbits %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n packbits-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l packbits

%check
%tox

%files -n python3-packbits -f %{pyproject_files}
%doc README.rst AUTHORS.rst

%changelog
%autochangelog
