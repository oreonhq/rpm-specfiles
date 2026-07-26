%global source0_hash ee708dfc5eefb8f23f57acfbbd0601b2fd089fcdb8172459fd3222e2a036fbc7

Name:         prwd
Version:      1.9.1
Release:      16%{?dist}
Summary:      A tool to print a reduced working directory
License:      ISC
URL:          http://tamentis.com/projects/prwd
Source0:      http://tamentis.com/projects/%{name}/files/%{name}-%{version}.tar.gz
Patch0: prwd-c99-1.patch
Patch1: prwd-c99-2.patch

BuildRequires:	gcc
BuildRequires:	make

%description
Most shells read $PS1 differently and have a very rigid way to display 
the current working directory. prwd allows you to have one way to handle 
the display of your working directory and use it across multiple shells. 
It also allows you to keep an eye on your current branch when you enter 
a project handled by git or mercurial.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Fix the typo here.
sed -i 's|commadn|command|g' ChangeLog

%build
%configure
%make_build

%install
%make_install

%check
make test

%files
%doc AUTHORS ChangeLog prwdrc.example TODO
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}rc.5*

%changelog
%autochangelog
