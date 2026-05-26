# when bootstrapping, we cannot yet use sphinx and pytest
# on RHEL, we don't need to build the documentation
%bcond docs %{undefined rhel}
%bcond tests 1

Name:           python-pygments
Version:        2.19.1
Release:        %autorelease
Summary:        Syntax highlighting engine written in Python

License:        BSD-2-Clause
URL:            https://pygments.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pygments/pygments-2.19.1.tar.gz
# https://github.com/pygments/pygments/issues/2992
# https://github.com/pygments/pygments/pull/3016
Patch0:         0001-Fix-test_lexer_classes-search-path.patch
# oreon url source checksums begin
%global source0_sha256 61c16d2a8576dc0649d9f39e089b5f02bcd27fba10d8fb4dcc28173f7a45151f
%global source0_file pygments-2.19.1.tar.gz
# oreon url source checksums end

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-lxml
%if %{undefined rhel}
# this is only used in tests.contrast.test_contrasts
# to avoid pulling this package into RHEL, the test is ignored in %%check
BuildRequires:  python%{python3_pkgversion}-wcag-contrast-ratio
%endif
%endif
%if %{with docs}
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-sphinx
# the sphinx config imports tests.contrast.test_contrasts:
BuildRequires:  python%{python3_pkgversion}-wcag-contrast-ratio
%endif


%global _description %{expand:
Pygments is a generic syntax highlighter suitable for use in code hosting,
forums, wikis or other applications that need to prettify source code.

Highlights are:

 * a wide range of over 500 languages and other text formats is supported
 * special attention is paid to details that increase highlighting quality
 * support for new languages and formats are added easily;
   most languages use a simple regex-based lexing mechanism
 * a number of output formats is available, among them HTML, RTF, LaTeX
   and ANSI sequences
 * it is usable as a command-line tool and as a library}

%description %_description


%package -n python%{python3_pkgversion}-pygments
Summary:        %{summary}
Provides:       pygmentize = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python%{python3_pkgversion}-pygments %_description


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pygments-2.19.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "61c16d2a8576dc0649d9f39e089b5f02bcd27fba10d8fb4dcc28173f7a45151f" || { echo "oreon: Source0 SHA256 mismatch for pygments-2.19.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n pygments-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pygments

install doc/pygmentize.1 -Dt %{buildroot}%{_mandir}/man1/

%if %{with docs}
%make_build -C doc html
rm doc/_build/html/.buildinfo
rm -rf doc/_build/html/_sources
chmod -x %{buildroot}%{_mandir}/man1/*.1
%endif


%if %{with tests}
%check
%pytest %{?rhel:--ignore tests/contrast/test_contrasts.py}
%endif


%files -n python%{python3_pkgversion}-pygments -f %{pyproject_files}
%doc AUTHORS CHANGES
%{?with_docs:%doc doc/_build/html}
%license LICENSE
%{_bindir}/pygmentize
%lang(en) %{_mandir}/man1/pygmentize.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.19.1-1
- Prepare for Oreon 11 (RP1)
