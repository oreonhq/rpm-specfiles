%global source0_hash b5f60fb47bbf5d8d762f134bcea0c388eba6b498342a682a21f1686545094b77

%bcond_without tests

Name:           python-dkimpy
Version:        1.1.8
Release:        %autorelease
Summary:        DKIM, ARC, and TLSRPT email signing and verification

License:        Zlib
URL:            https://launchpad.net/dkimpy
Source:         %{pypi_source dkimpy}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  openssl
%endif

%global _description %{expand:
dkimpy is a library that implements DKIM (DomainKeys Identified Mail)
email signing and verification.}

%description %_description

%package -n     python3-dkimpy
Summary:        %{summary}

%description -n python3-dkimpy %_description

%pyproject_extras_subpkg -n python3-dkimpy ARC,asyncio,ed25519

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n dkimpy-%{version}

# Drop shebang for these files, as we don't need them
sed -e "s|^#!/usr/bin/.*python$||" -i dkim/{arcsign.py,arcverify.py,dkimsign.py,dkimverify.py,dknewkey.py}

%generate_buildrequires
%pyproject_buildrequires -x ARC,asyncio,ed25519,testing

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l dkim

%check
%pyproject_check_import
%if %{with tests}
%{py3_test_envvars} %{python3} -m unittest -v
%endif

%files -n python3-dkimpy -f %{pyproject_files}
%doc ChangeLog README.md
%{_bindir}/arcsign
%{_bindir}/arcverify
%{_bindir}/dkimsign
%{_bindir}/dkimverify
%{_bindir}/dknewkey
%{_mandir}/man1/arcsign.1*
%{_mandir}/man1/arcverify.1*
%{_mandir}/man1/dkimsign.1*
%{_mandir}/man1/dkimverify.1*
%{_mandir}/man1/dknewkey.1*

%changelog
%autochangelog
