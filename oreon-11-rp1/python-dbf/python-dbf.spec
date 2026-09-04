%global source0_hash 940272a72ac27d16a1db69aafef820684012cc3553ffe9875d5cd2e3a9cb69dc

%global pypi_name dbf
%global sum Pure python package for reading/writing dBase, FoxPro, and Visual FoxPro .dbf
%global desc Pure python package for reading/writing dBase, FoxPro, and Visual FoxPro .dbf\
files (including memos)\
\
Currently supports dBase III, Clipper, FoxPro, and Visual FoxPro tables. Text is\
returned as unicode, and codepage settings in tables are honored. Memos and Null\
fields are supported.

Name:           python-%{pypi_name}
Version:        0.99.3
Release:        13%{?dist}
Summary:        %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://pypi.python.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         prevent-synthax-error.patch
Patch1:         remove-distutil.patch

BuildArch:      noarch

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{sum}
BuildRequires:  python3-devel
Requires:       python3-aenum

%description -n python3-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pypi_name}-%{version}
# Correct line endings for setup.py
sed -i "s|\r||g" setup.py
%autopatch -p1
rm -f dbf/ver_32.py
rm -f dbf/ver_2.py
sed -i "s|\r||g" dbf/README.md

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc dbf/README.md
%license dbf/LICENSE

%changelog
%autochangelog
