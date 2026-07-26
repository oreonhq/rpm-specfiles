%global source0_hash f3c547a172c36ba26b8614c809f5823bc6199623ec6204ec7c3bce29037f7758

# Generated from ruby-vips-2.0.17.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby-vips

Name: rubygem-%{gem_name}
Version: 2.2.5
Release: 2%{?dist}
Summary: Ruby extension for the vips image processing library
License: MIT
URL: http://github.com/libvips/ruby-vips
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout http://github.com/libvips/ruby-vips
# cd ruby-vips && git archive -v -o ruby-vips-2.2.5-spec.tar.gz v2.2.5 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz

Requires: (libvips.so.42()(64bit) if libc.so.6()(64bit))
Requires: (libvips.so.42 if libc.so.6)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(ffi)
BuildRequires: rubygem(logger)
BuildRequires: rubygem(rspec) >= 3.3
BuildRequires: (libvips.so.42()(64bit) if libc.so.6()(64bit))
BuildRequires: (libvips.so.42 if libc.so.6)
BuildArch: noarch

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

%check
( cd .%{gem_instdir}
ln -s %{_builddir}/spec .
rspec spec
)

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/TODO
%{gem_instdir}/ruby-vips.gemspec
%{gem_instdir}/VERSION
%{gem_instdir}/example

%changelog
%autochangelog
