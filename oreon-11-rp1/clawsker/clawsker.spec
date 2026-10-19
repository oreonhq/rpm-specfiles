%global source0_hash 586b91a8ca8cd5bddcc166935b3ef109269817aec7b93bdff90b31361949ffba
Name:           clawsker
Version:        1.4.1
Release:        4%{?dist}
Summary:        Dialog to edit Claws Mail's hidden preferences
License:        GPL-3.0-or-later
URL:            http://www.claws-mail.org/clawsker
Source0:        http://www.claws-mail.org/tools/%{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       claws-mail
# oreon:deps
BuildRequires:  /usr/bin/pod2man
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
Clawsker is a Perl-GTK3 applet to edit hidden preferences for Claws Mail, and 
to do it in a safe and user friendly way, preventing users from raw editing of 
configuration files.

Claws Mail is a fast and lightweight Mail User Agent by the Claws Mail Team.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

make %{?_smp_mflags}
%install
%make_install PREFIX=%{_prefix}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
