%global source0_hash 9a4257a807b3f5803e3afc89c52c5a6372727dd1b1bb63c08e334d841177729b

#global commit 446e6e382f7e79744549f72436cd5407cefac8db
#global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           dropbox-api-command
Version:        2.13
Release:        19%{?dist}
Summary:        Dropbox API wrapper command

License:        MIT
URL:            https://github.com/s-aska/%{name}
Source0:        https://github.com/s-aska/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
A command line tool to manage a directory synced with Dropbox.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{_bindir}/dropbox-api
%{_bindir}/upload-to-dropbox
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
