%global source0_hash f5afcdb6823c570760be9692f33d0642a20cd86925b4cab721d108050d0f8201
%global srcname visidata
Name:           %{srcname}
Version:        3.4
Release:        1%{?dist}
Summary:        Terminal interface for exploring and arranging tabular data
License:        GPL-3.0-only
URL:            https://visidata.org
Source0:        https://files.pythonhosted.org/packages/source/v/%{name}/%{name}-%{version}.tar.gz
Patch:          0001-Remove-extra-copy-of-man-page.patch
Patch:          0002-Fix-test-on-Python-3.14.patch
BuildArch:      noarch
ExcludeArch: %{ix86}
Requires:       python3-%{srcname} = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-visidata = %{version}-%{release}
# /oreon:deps
%description
VisiData is an interactive multitool for tabular data. It combines the clarity
of a spreadsheet, the efficiency of the terminal, and the power of Python, into
a lightweight utility which can handle millions of rows with ease.

%package -n     python3-%{srcname}
Summary:        Terminal interface for exploring and arranging tabular data
Recommends: python3dist(PyYAML)
Recommends: python3dist(datapackage)
Recommends: python3dist(dnslib)
Recommends: python3dist(dpkt)
Recommends: python3dist(fonttools)
Recommends: python3dist(h5py)
Recommends: python3dist(lxml)
Recommends: python3dist(mapbox-vector-tile)
Recommends: python3dist(namestand)
Recommends: python3dist(numpy)
Recommends: python3dist(openpyxl)
Recommends: python3dist(pandas) >= 1.5.3
Recommends: python3dist(pdfminer-six)
Recommends: python3dist(psycopg2)
Recommends: python3dist(pypng)
Recommends: python3dist(pyshp)
Recommends: python3dist(requests)
Recommends: python3dist(sas7bdat)
Recommends: python3dist(savReaderWriter)
Recommends: python3dist(tabulate)
Recommends: python3dist(vobject)
Recommends: python3dist(wcwidth)
Recommends: python3dist(xlrd)
Recommends: python3dist(xport)
%description -n python3-%{srcname}
VisiData is an interactive multitool for tabular data. It combines the clarity
of a spreadsheet, the efficiency of the terminal, and the power of Python, into
a lightweight utility which can handle millions of rows with ease.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%pyproject_wheel
%install
%pyproject_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{srcname}.desktop
%oreon_autofiles main usr/lib/python3*/site-packages/visidata* usr/lib64/python3*/site-packages/visidata* usr/bin/*

%check

mkdir HOME
touch HOME/.visidatarc  # Needed for TestCommands.test_baseCommands
export HOME=$PWD/HOME
%{pytest}
%files
%files -n python3-visidata -f %{oreon_filedir}/python3-visidata.list

%changelog

%autochangelog
