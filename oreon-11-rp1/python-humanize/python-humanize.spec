%global source0_hash 1dd098483eb1c7ee8e32eb2e99ad1910baefa4b75c3aff3a82f4d78688993b10

%bcond_without check

Name:           python-humanize
Version:        4.16.0
Release:        %autorelease
Summary:        Turns dates in to human readable format, e.g '3 minutes ago'

License:        MIT
URL:            https://github.com/python-humanize/humanize
Source0:        https://files.pythonhosted.org/packages/source/h/humanize/humanize-4.15.0.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description\
This modest package contains various common humanization utilities, like turning\
a number into a fuzzy human readable duration ('3 minutes ago') or into a human\
readable size or throughput.\

%description %_description

%package -n python3-humanize
Summary: %summary

%description -n python3-humanize
This modest package contains various common humanization utilities, like turning
a number into a fuzzy human readable duration ('3 minutes ago') or into a human
readable size or throughput.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n humanize-%{version}

# Remove shebangs from libs.
for lib in src/humanize/filesize.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new && mv $lib.new $lib
done

# Remove .po files
find -name '*.po' -delete

# Don't run coverage report during %%check
sed -i '/pytest-cov/d' pyproject.toml
sed -i '/core:coverage.exceptions.CoverageWarning/d' pyproject.toml
sed -Ei 's/ ?--cov(-[^ ]+)? +[^ ]+//g' tox.ini

%generate_buildrequires
%pyproject_buildrequires %{?with_check:-t}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files humanize

%if %{with check}
%check
%pytest
%endif

%files -n python3-humanize -f %{pyproject_files}
%doc README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.15.0-1
- Prepare for Oreon 11 (RP1)
