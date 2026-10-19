%global source0_hash 1bfb4351c3e49681a875dab937c25b6b38e4bf8a8cd64bcba1954300242578cb
%global pkg auto-complete
Name:           emacs-%{pkg}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Emacs auto-complete package
License:        GPL-3.0-or-later
URL:            https://github.com/%{pkg}/%{pkg}/
Source0:        https://github.com/%{pkg}/%{pkg}//archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-popup
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs
BuildRequires:  emacs-popup
# /oreon:deps
%description
Auto-Complete is an intelligent auto-completion extension for Emacs. It extends
the standard Emacs completion interface and provides an environment that allows
users to concentrate more on their own work.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version}

%build

for i in *.el; do
    %{_emacs_bytecompile} $i
done
%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 *.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el
%oreon_autofiles main

%check

emacs --batch -q --no-site-file --no-splash \
    -L $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/ \
    -l tests/run-test.el \
    -f ert-run-tests-batch-and-exit
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
