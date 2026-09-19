%global source0_hash 527871f17d7aea96e449a97d95ae85661d74476c2f6216e25b279d3ab7bfd73b

%global giturl  https://github.com/victorhge/iedit

Name:           emacs-iedit
Version:        0.9.9.9.9
Release:        10%{?dist}
Summary:        Edit multiple regions simultaneously in Emacs

License:        GPL-3.0-or-later
URL:            https://www.emacswiki.org/emacs/Iedit
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/iedit-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildArch:      noarch

BuildRequires:  emacs-nw
BuildRequires:  make

Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}

%description
This package includes Emacs minor modes (iedit-mode and iedit-rectangle-mode)
based on an API library (iedit-lib) and allows you to alter one occurrence of
some text in a buffer (possibly narrowed) or region, and simultaneously have
other occurrences changed in the same way, with visual feedback as you type.

iedit-mode is a great alternative to built-in replace commands:

- A more intuitive way to alter all the occurrences at once
- Visual feedback
- Fewer keystrokes in most cases
- Optionally preserve case

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n iedit-%{version}

%conf
# Fix permissions
chmod 0644 iedit-demo.gif

%build
%make_build

%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}/iedit
install -m 644 *.el{,c} %{buildroot}/%{_emacs_sitelispdir}/iedit

mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv %{buildroot}/%{_emacs_sitelispdir}/iedit/iedit-autoloads.el \
  %{buildroot}%{_emacs_sitestartdir}

%files
%doc README.org iedit-demo.gif
%{_emacs_sitelispdir}/iedit/
%{_emacs_sitestartdir}/iedit-autoloads.el

%changelog
%autochangelog
