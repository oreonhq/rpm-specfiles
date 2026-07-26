%global source0_hash 76cbb014473672d1c384922857f8fbc1f6f7774f74f784149ad88751854ecfdf

Name:           thefuck
Version:        3.32
Release:        %autorelease
Summary:        App that corrects your previous console command
License:        MIT
URL:            https://github.com/nvbn/thefuck
Source0:        https://github.com/nvbn/%{name}/archive/%{version}.tar.gz

# https://github.com/nvbn/thefuck/pull/1248
Patch0:         thefuck-support-python-3.11.patch
# https://github.com/nvbn/thefuck/pull/1474
Patch1:         thefuck-fix-pytest8.patch
# https://github.com/nvbn/thefuck/pull/1437
Patch2:         thefuck-replace-mock.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%description
This application corrects your previous console command.
If you use BASH, you should add these lines to your .bashrc:
alias fuck='eval $(thefuck $(fc -ln -1)); history -r'
alias FUCK='fuck'
For other shells please check /usr/share/doc/thefuck/README.md

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
%py3_shebang_fix *.py

# Cleanup requirements for release and functional tests
grep -Ev '^(flake8|mock|pexpect|pypandoc|pytest-benchmark|pytest-docker-pexpect|twine)\s*$' requirements.txt | tee requirements-filtered.txt

# Don't generate (unfiltered) dependencies for tox:
sed -Ei 's/[-]rrequirements\.txt//' tox.ini

%generate_buildrequires
%pyproject_buildrequires -t requirements-filtered.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files thefuck

%check
%tox

%files -n thefuck -f %{pyproject_files}
%license LICENSE.md
%doc README.md
%{_bindir}/fuck
%{_bindir}/thefuck

%changelog
%autochangelog
