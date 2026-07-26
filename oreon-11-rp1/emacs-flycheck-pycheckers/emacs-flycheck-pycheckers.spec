%global source0_hash 8403bf5a550673e05895c79e6f9a961d1a72be0286ecf76b15d6d54a34746964

%global pkg flycheck-pycheckers

Name:           emacs-%{pkg}
Version:        0.16
Release:        7%{?dist}
Summary:        Multiple syntax checker for Python in Emacs, using Flycheck

License:        GPL-3.0-or-later
URL:            https://github.com/msherry/%{pkg}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el
# Fix arguments in call to define-obsolete-variable-alias (since Emacs 28, see
# also https://github.com/msherry/flycheck-pycheckers/pull/60)
Patch0:         %{name}-0.15-emacs28.patch

BuildRequires:  emacs
BuildRequires:  emacs-flycheck
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-flycheck
BuildArch:      noarch

%description
This package provides a way to run multiple syntax checkers on Python code, in
parallel. The list of supported checkers includes:
* pylint
* flake8
* pep8
* pyflakes
* mypy
* bandit
This is an alternative way of running multiple Python syntax checkers in
Flycheck that doesn't depend on Flycheck's chaining mechanism.

Flycheck is opinionated about what checkers should be run, and chaining is
difficult to get right. This package assumes that the user knows what they want,
and can configure their checkers accordingly — if they want to run both flake8
and pylint, that's fine.

This also allows us to run multiple syntax checkers in parallel, rather than
sequentially.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version}

# Fix shebang
sed -e 's|^#!.*|#!%{__python3}|' bin/pycheckers.py >bin/pycheckers.py.new && \
touch -r bin/pycheckers.py bin/pycheckers.py.new && \
mv bin/pycheckers.py.new bin/pycheckers.py

%build
%{_emacs_bytecompile} %{pkg}.el

%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
cp -a bin/ $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
chmod 0755  $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/bin/pycheckers.py

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el

%files
%doc pycheckers-EXAMPLE README.md
%license LICENSE
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el

%changelog
%autochangelog
