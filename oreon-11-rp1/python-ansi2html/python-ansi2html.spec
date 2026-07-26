%global source0_hash 3453bf87535d37b827b05245faaa756dbab4ec3d69925e352b6319c3c955c0a5

# Run tests by default
%bcond_without tests

%global srcname ansi2html

Name:       python-%{srcname}
Version:    1.9.2
Release:    8%{?dist}
Summary:    Python module that converts text with ANSI color to HTML
# While the project was previously licensed as GPLv3+, it is now LGPLv3.
# See https://github.com/pycontribs/ansi2html/issues/72 and also
# https://github.com/pycontribs/ansi2html/issues/188 for more info.
# In these issues, all of the previous contributors agreed to relicense their code.
License:    LGPL-3.0-only
URL:        http://github.com/pycontribs/%{srcname}
Source:     %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  python3-devel
# Needed for building manpages
BuildRequires:  /usr/bin/a2x

%global _description %{expand:
The ansi2html module can convert text with ANSI color codes to HTML.}

%description %{_description}

%package -n python3-%{srcname}
Summary:    %{summary}
%dnl colorized-logs also provides %{_bindir}/ansi2html and %{_mandir}/man1/ansi2html.1*
Conflicts:  colorized-logs

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
# The -t is set if %%{with_tests} is true
%pyproject_buildrequires %{?with_tests:-t}

%build
# Build manpages
a2x \
    --conf-file=man/asciidoc.conf \
    --attribute="manual_package=ansi2html" \
    --attribute="manual_title=ansi2html Manual" \
    --attribute="manual_version=%{version}" \
    --format=manpage -D man \
     man/ansi2html.1.txt

# Build wheel
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

# Install manpage
install -Dpm 644 man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1

%check
%if %{with tests}
%tox
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md docs/*.md
%license LICENSE
%{_bindir}/%{srcname}
%{_mandir}/man1/%{srcname}.1*

%changelog
%autochangelog
