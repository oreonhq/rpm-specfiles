%global source0_hash 1b5b863777dad11462dfc3c9d7bb7878c8671a42131b19bbe4e112943b731e51
Name:           perl-autobox-List-Util
Version:        20090629
Release:        1%{?dist}
Summary:        Bring the List::Util functions to autobox
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/autobox-List-Util
Source0:        https://cpan.metacpan.org/modules/by-module/autobox/autobox-List-Util-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(List::Util)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(autobox)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
autobox::List::Util brings all of the functions from List::Util to arrays as
methods.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n autobox-List-Util-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
