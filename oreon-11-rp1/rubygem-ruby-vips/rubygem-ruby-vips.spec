%global source0_hash f3c547a172c36ba26b8614c809f5823bc6199623ec6204ec7c3bce29037f7758
%global gem_name ruby-vips
Name: rubygem-%{gem_name}
Version: 2.2.5
Release:        2%{?dist}
Summary:        Ruby extension for the vips image processing library
License: MIT
URL: http://github.com/libvips/ruby-vips
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}-spec.tar.gz
Requires: (libvips.so.42()(64bit) if libc.so.6()(64bit))
Requires: (libvips.so.42 if libc.so.6)
BuildArch: noarch
# oreon:deps
BuildRequires:  (libvips.so.42 if libc.so.6)
BuildRequires:  (libvips.so.42()(64bit) if libc.so.6()(64bit))
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(ffi)
BuildRequires:  rubygem(logger)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
ruby-vips is a binding for the libvips image processing library. It is fast
and it can process large images without loading the whole image in memory.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
ln -s %{_builddir}/spec .
rspec spec
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ruby-vips-doc -f %{oreon_filedir}/rubygem-ruby-vips-doc.list

%changelog

%autochangelog
