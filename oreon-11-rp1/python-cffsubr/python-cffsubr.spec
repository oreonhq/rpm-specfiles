%global source0_hash 2c321b6807bd95856d921ed9dce8506495cf49fc7a89a63cb942e8bece13addd
Name:           python-cffsubr
Version:        0.4.0
Release:        1%{?dist}
Summary:        Standalone CFF subroutinizer based on the AFDKO tx tool
License:        Apache-2.0
URL:            https://pypi.org/project/cffsubr
Source0:        https://files.pythonhosted.org/packages/source/c/cffsubr/cffsubr-0.4.0.tar.gz
Source1:        cffsubr.1
BuildArch:      noarch
%global txbin /usr/bin/tx
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cffsubr = %{version}-%{release}
# /oreon:deps
%description
Standalone CFF subroutinizer based on the AFDKO tx tool.

%package -n python3-cffsubr
Summary:        Standalone CFF subroutinizer based on the AFDKO tx tool
Requires:       ((adobe-afdko >= 4.0.3) with (adobe-afdko < 5~~))
%description -n python3-cffsubr
Standalone CFF subroutinizer based on the AFDKO tx tool.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n cffsubr-%{version} -p1

# Do not build the extension, which is a copy of the “tx” executable from
# adobe-afdko. Patch out the custom build backend, which would have generated
# dependencies needed for building the extension.
sed -r -i 's/(ext_modules=)/# \1/' setup.py
sed -r -i 's/^(build-backend|backend-path)/# \1/' pyproject.toml

# Remove bundled adobe-afdko:
rm -rf external

%build

%pyproject_wheel
%install
%pyproject_install
install -d "%{buildroot}$(dirname '%{txbin}')"
ln -s '%{txbin}' '%{buildroot}%{txbin}'
ln -s '%{buildroot}%{txbin}' %{buildroot}/%{python3_sitelib}/cffsubr/tx
symlinks -c -o %{buildroot}/%{python3_sitelib}/cffsubr/tx
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'
%oreon_autofiles python3-cffsubr usr/lib/python3*/site-packages/cffsubr* usr/lib64/python3*/site-packages/cffsubr* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cffsubr* usr/lib64/python3*/site-packages/cffsubr* usr/bin/*

%check

%pytest
%files
%files -n python3-cffsubr -f %{oreon_filedir}/python3-cffsubr.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.0-3
- Prepare for Oreon 11 (RP1)
