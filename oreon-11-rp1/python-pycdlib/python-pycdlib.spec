%global source0_hash 39e95a0d90cee4ecc3472d0fcf7167d2a5c30b209dc4b156e39e0cdc441529f2

%global desc Pycdlib is a pure python library for reading, writing, and\
otherwise manipulating ISO9660 files.  It is focused on speed, correctness,\
and conformance to the various standards around ISO9660, including ISO9660\
itself, the Joliet extensions, the Rock Ridge extensions, the El Torito boot\
extensions, and UDF.

%global srcname pycdlib

Summary:        A pure python ISO9660 read and write library
Name:           python-%{srcname}
Version:        1.15.0
Release:        6%{?dist}
License:        LGPL-2.0-only
URL:            https://github.com/clalancette/%{srcname}
Source0:        https://github.com/clalancette/pycdlib/archive/v1.15.0/pycdlib-1.15.0.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  genisoimage
BuildRequires:  python3-pytest

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%package -n %{srcname}-tools
Summary:        Tools that rely on %{srcname}
Requires:       python3-%{srcname} = %{version}-%{release}

%description -n %{srcname}-tools
Some tools that use the %{srcname} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
PYCDLIB_TRACK_WRITES=1 py.test-%{python3_version} \
                       -k " not test_hybrid_rr \
                       and not test_hybrid_joliet_rr_and_eltorito \
                       and not test_hybrid_sevendeepdirs \
                       and not test_parse_rr \
                       and not test_parse_joliet_and_rr \
                       and not test_parse_joliet_rr_and_eltorito \
                       and not test_parse_sevendeepdirs \
                       and not test_parse_everything \
                       and not test_parse_same_dirname_different_parent \
                       and not test_parse_duplicate_rrmoved_name \
                       and not test_parse_eltorito_rr \
                       and not test_parse_overflow_root_dir_record \
                       and not test_parse_deep_rr_symlink \
                       and not test_parse_joliet_encoded_system_identifier" \
                       -v tests

%files -n python3-%{srcname} -f %{pyproject_files}
%license COPYING
%doc README.md examples/

%files -n %{srcname}-tools
%license COPYING
%{_bindir}/pycdlib-explorer
%{_bindir}/pycdlib-extract-files
%{_bindir}/pycdlib-genisoimage
%{_mandir}/man1/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.15.0-6
- Prepare for Oreon 11 (RP1)
