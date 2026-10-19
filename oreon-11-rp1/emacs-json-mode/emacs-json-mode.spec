%global source0_hash 1d82bcdebb25b29fa1d7ab7aa90b379bc3f9d9ab5699bc3484345c1e8a97eb72
%global pkg json-mode
Name:           emacs-%{pkg}
Version:        1.9.2
Release:        1%{?dist}
Summary:        Major mode for editing JSON files with Emacs
License:        GPL-3.0-or-later
URL:            https://github.com/joshwnj/%{pkg}
Source0:        https://github.com/joshwnj/%{pkg}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-json-reformat
Requires:       emacs-json-snatcher
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs
BuildRequires:  emacs-json-reformat
BuildRequires:  emacs-json-snatcher
# /oreon:deps
%description
Major mode for editing JSON files.

Extends the builtin js-mode to add better syntax highlighting for JSON.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version}

%build

%{_emacs_bytecompile} %{pkg}.el
%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
