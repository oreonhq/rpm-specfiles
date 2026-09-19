%global source0_hash c92551ab2be318320c3e002bdd92d2bbdf148749e31c8c6449c431d04db2052a

Name:           python-pykdumpfile
Version:        0.5.5.1
Release:        %autorelease
Summary:        Python bindings to libkdumpfile

License:        GPL-2.0-or-later
URL:            https://github.com/ptesarik/pykdumpfile
Source:         %{pypi_source pykdumpfile}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  gcc
BuildRequires:  libkdumpfile-devel

%global _description %{expand:
Bindings to the libkdumpfile shared library.}

%description %_description

%package -n     python3-pykdumpfile
Summary:        %{summary}
# provide an upgrade path until Fedora 41 is EOL
# we don't need to handle EL since python3-libkdumpfile is not published
%if 0%{?fedora} && 0%{?fedora} <= 43
Obsoletes:      python3-libkdumpfile < 0.5.5-1
%endif

%description -n python3-pykdumpfile %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pykdumpfile-%{version}
# These are meant for Python 2 and wont' byte-compile
rm {addrxlat,kdumpfile}/defs_py2.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l addrxlat kdumpfile

%check
%pyproject_check_import
%pytest -v

%files -n python3-pykdumpfile -f %{pyproject_files}
%doc README.md
%{python3_sitearch}/_addrxlat%{python3_ext_suffix}
%{python3_sitearch}/_kdumpfile%{python3_ext_suffix}

%changelog
%autochangelog
