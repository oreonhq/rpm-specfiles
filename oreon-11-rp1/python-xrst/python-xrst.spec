%global source0_hash 720e254fe6e7195f0e5057ee5a1062d1806ac816e43f7604a11e4020b8d9e806

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/

# Fedora Release starts with 1; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/
Name:           python-xrst
Version:        2026.0.0
Release:        2%{?dist}
Summary:        Extract Sphinx RST Files

License:        GPL-3.0-or-later
URL:            https://github.com/bradbell/xrst
Source:         %{url}/archive/%{version}/python-xrst-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a sphinx wrapper that extracts RST files from source code
and then runs sphinx to obtain html, tex, or pdf output files.
It includes automatic processing and commands that make sphinx easier to use.}

# First %%description command.
%description %_description

%package -n python3-xrst
Summary:        %{summary}

# Second %%description command.
# What is the difference between the two %%description commands ?
%description -n python3-xrst %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n xrst-%{version}
#
# Suppress spelling warnings during tox because this system
# may use a different dictionary than is used for xrst development.
cat << EOF > temp.sed
s|'sphinx_rtd_theme'|&, '--suppress_spell_warnings'|
EOF
sed -i pytest/test_rst.py -f temp.sed 
#
%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files xrst

# -----------------------------------------------------------------------------
# Do after installs above so don't get an rpmlint warning about using buildroot
#
# create %%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man1
#
# create build/rst/run_xrst.rst
%{python3} -m xrst \
   --rst_only --group_list default user --suppress_spell_warnings
#
# install %%{_mandir}/man1/xrst.1
%{python3} bin/rst2man.py \
   build/rst/run_xrst.rst %{buildroot}/%{_mandir}/man1/xrst.1
# -----------------------------------------------------------------------------

%check
%tox
#

%files -n python3-xrst -f %{pyproject_files}
%doc readme.md
%license gpl-3.0.txt

# xrst executable
%{_bindir}/xrst

# xrst.1 man page
%{_mandir}/man1/xrst.1*

%changelog
%autochangelog
