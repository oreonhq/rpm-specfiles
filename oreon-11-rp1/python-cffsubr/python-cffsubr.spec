# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 2c321b6807bd95856d921ed9dce8506495cf49fc7a89a63cb942e8bece13addd
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           python-cffsubr
Version:        0.4.0
Release:        3%{?dist}
Summary:        Standalone CFF subroutinizer based on the AFDKO tx tool

# The entire source is Apache-2.0, except:
# - These are derived from fonts licened OFL-1.1, but are not packaged, so they
#   do not contribute to the licenses of the binary RPMs:
#   • tests/data/SourceSansPro-Regular.subset.ttx
#   • tests/data/SourceSansVariable-Regular.subset.ttx
# See NOTICE.
License:        Apache-2.0
URL:            https://pypi.org/project/cffsubr
Source0:        https://files.pythonhosted.org/packages/source/c/cffsubr/cffsubr-0.4.0.tar.gz
# Written for Fedora in groff_man(7) format based on the output of “cffsubr --help”
Source1:        cffsubr.1

BuildArch:      noarch

BuildRequires:  python3-devel

%global txbin /usr/bin/tx
# For the unbundled “tx” executable:
BuildRequires:  ((adobe-afdko >= 4.0.3) with (adobe-afdko < 5~~))
BuildRequires:  symlinks

%description
Standalone CFF subroutinizer based on the AFDKO tx tool.

%generate_buildrequires
%pyproject_buildrequires -x testing

%package -n python3-cffsubr
Summary:        %{summary}

# For the unbundled “tx” executable:
Requires:       ((adobe-afdko >= 4.0.3) with (adobe-afdko < 5~~))

%description -n python3-cffsubr
Standalone CFF subroutinizer based on the AFDKO tx tool.

%prep
%oreon_verify_sources
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
%pyproject_save_files -l cffsubr

# Workaround to prevent a dangling symlink:
install -d "%{buildroot}$(dirname '%{txbin}')"
ln -s '%{txbin}' '%{buildroot}%{txbin}'

# Build a relative symbolic link:
ln -s '%{buildroot}%{txbin}' %{buildroot}/%{python3_sitelib}/cffsubr/tx
symlinks -c -o %{buildroot}/%{python3_sitelib}/cffsubr/tx

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'

%check
%pytest

%files -n python3-cffsubr -f %{pyproject_files}
%doc README.md

# Symbolic link to the “tx” executable; we patched out building a separate copy
# for the Python package, so the Python build does not know about this and we
# must list it explicitly.
%{python3_sitelib}/cffsubr/tx
# This was just a workaround:
%exclude %{txbin}

%{_bindir}/cffsubr
%{_mandir}/man1/cffsubr.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.0-3
- Prepare for Oreon 11 (RP1)
