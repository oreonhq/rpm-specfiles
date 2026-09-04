%global source0_hash fe16f839279e8baff96dcead55feb03997aebdaa3cee7a421dadc8e7cb8c1581

Name:           taskopen
Version:        2.0.3
Release:        %autorelease
Summary:        Script for taking notes and open urls with taskwarrior

License:        GPL-2.0-or-later
URL:            https://github.com/ValiValpas/taskopen
Source0:        https://github.com/ValiValpas/taskopen/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires: perl-generators

Requires:       task

%description
taskopen allows you to link almost any file, webpage or command to a
taskwarrior task by adding a filepath, web-link or uri as an annotation. Text
notes, images, PDF files, web addresses, spreadsheets and many other types of
links can then be filtered, listed and opened by using taskopen. Some actions
are sane defaults, others can be custom-configured, and everything else will
use your systems mime-types to open the link.

Arbitrary commands can be used with taskopen at the CLI, acting on the link
targets, enhancing listings and even executing annotations as commands.

Run 'taskopen -h' or 'man taskopen' for further details. The following sections
show some (very) basic usage examples.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Left overs?
rm -vf doc/html/*.orig

%build
# Nothing to do here

%install
%make_install PREFIX=%{_prefix}

# Wrong location, we'll intall it ourselves
rm -rfv $RPM_BUILD_ROOT/%{_datadir}/taskopen/doc

%files
%doc examples doc/html/
%{_bindir}/%{name}
%{_mandir}/man1/taskopen.1*
%{_mandir}/man5/taskopenrc.5*
%{_datadir}/%{name}/

%changelog
%autochangelog
