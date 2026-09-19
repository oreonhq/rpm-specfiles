%global source0_hash 2aaee14bbc2f63619d6ebc541df24b9c60aa24bcc1c424046957964e1074475d

Name:		editorconfig-emacs
Version:	0.10.1
Release:	5%{?dist}
Summary:	EditorConfig plugin for emacs
License:	GPL-3.0-or-later
URL:		https://github.com/editorconfig/%{name}
Source0:	https://github.com/editorconfig/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	editorconfig-init.el
BuildRequires:	emacs
BuildRequires:	texinfo
BuildArch:	noarch
Requires:	emacs(bin) >= %{_emacs_version}

%description
This is the EditorConfig plugin for emacs.  With this plugin
installed, emacs will automatically respect coding style settings
found in an .editorconfig file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build

# The tarball includes an Eask file, but eask is not packaged for
# Fedora (and is unlikely to be, since it depends on multiple NPM
# modules).  Use a direct %{_emacs_bytecompile} instead.
#
%{_emacs_bytecompile} *.el

# Build info page
#
make doc/editorconfig.info

%install
%{__mkdir_p} %{buildroot}%{_emacs_sitelispdir}
%{__install} -p -m 644 *.el *.elc %{buildroot}%{_emacs_sitelispdir}/
%{__mkdir_p} %{buildroot}%{_emacs_sitestartdir}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/
%{__mkdir_p} %{buildroot}%{_infodir}
%{__install} -p -m 644 doc/editorconfig.info %{buildroot}%{_infodir}/

%files
%doc CONTRIBUTORS CHANGELOG.md README.md
%license LICENSE
%{_emacs_sitelispdir}/editorconfig*.el
%{_emacs_sitelispdir}/editorconfig*.elc
%{_emacs_sitestartdir}/editorconfig-init.el
%{_infodir}/editorconfig*

%changelog
%autochangelog
