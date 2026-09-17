%global source0_hash eab1e6a471a8212572e586e2aaf34ddbecdec4b8e3aec8084aaea1ba3e020d24

Name:           irclog2html
Version:        4.0.0
Release:        5%{?dist}
Summary:        A script to convert IRC logs to HTML and other formats

License:        GPL-2.0-or-later
URL:            http://mg.pov.lt/irclog2html/
Source0:        https://github.com/mgedmin/irclog2html/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
irclog2html is a nice IRC log parser and colorizer that will do the most common
things necessary to make an IRC log readable in a web browser. It can export to
many different HTML formats, and can export MediaWiki pipe-table syntax.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
echo "You may need the irclog.css file. It is available at
  %{_datadir}/%{name}/irclog.css
" > README.fedora

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

mkdir -p %{buildroot}%{_datadir}/%{name}
install -Dpm 0644 src/%{name}/irclog.css %{buildroot}%{_datadir}/%{name}

%pyproject_save_files -l %{name}

%files -n %files -n irclog2html -f %{pyproject_files}
%doc CHANGES.rst HACKING.rst README.rst README.fedora
%license COPYING
%{_bindir}/%{name}
%{_bindir}/irclogsearch
%{_bindir}/irclogserver
%{_bindir}/logs2html
%{_datadir}/%{name}/

%changelog
%autochangelog
