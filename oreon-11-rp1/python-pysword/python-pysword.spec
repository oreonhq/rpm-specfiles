%global source0_hash f6cbdb1075a503440c30707f7202fa6dd41ae7d48c0e9d9177618e6da456ecf1

%global srcname pysword
%global sum Open source python API wrapper for Sword Bible files
%global desc %{expand: A native Python reader of the SWORD Project Bible Modules.
Reads SWORD bible files (not commentaries etc.)
Detection of locally installed Swrod bible modules.
Supports all known SWORD module formats (ztext, ztext4, rawtext, rawtext4)
Read from zipped modules, like those available from
http://www.crosswire.org/sword/modules/ModDisp.jsp?modType=Bibles
Cleans the extracted text of OSIS, GBF or ThML tags. 
Supports both python 2 and 3 (tested with 2.7 and 3.5) }

Summary: %{sum}
Name: python-%{srcname}
Version: 0.2.8
Release: 17%{?dist}
Source0: https://gitlab.com/tgc-dk/%{srcname}/repository/archive.tar.gz?ref=%{version}#/%{srcname}-%{version}.tar.gz
Source1: testdata-0.2.8.tar.gz
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
BuildArch: noarch

URL: https://gitlab.com/tgc-dk/pysword

BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}
# Remove this in Fedora 38:
Obsoletes:      python-%{srcname} < 0.2.7-7

%description -n python3-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
%autosetup -N -T -D -a 1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pysword

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
