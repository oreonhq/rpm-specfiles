%global source0_hash none

%define name2 wp

Name:       wp-cli
Version:    2.4.0
Release:    15%{?dist}
Summary:    The command line interface for WordPress
License:    MIT
URL:        http://%{name}.org/
Source0:    https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.phar
Source1:    LICENSE
Source2:    wp.1
BuildArch:  noarch

%description
WP-CLI is the command-line interface for WordPress.
You can update plugins, configure multisite installations
and much more, without using a web browser.

%prep
chmod +x %{SOURCE0}
{
    echo '.TH "WP" "1"'
    php %{SOURCE0} --help
} \
    | sed -e 's/^\([A-Z ]\+\)$/.SH "\1"/' \
    | sed -e 's/^  wp$/wp \\- The command line interface for WordPress/' \
> %{SOURCE2}

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name2}
cp -f %SOURCE1 LICENSE
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/

%files
%license LICENSE
%{_bindir}/%{name2}
%{_mandir}/man1/wp.1*

%changelog
%autochangelog
