%global source1_hash b744e8c22c021bd9ae66e3bc1b1ced64c082d0bdb99fc87d10937a7f8c268086
%global source0_hash 29395dfd76badcabb6403ee5aff6f681e867074f8f28ce08d78661e9e4a351c4
%global gem_name mini_magick
Name: rubygem-%{gem_name}
Version: 5.3.1
Release:        1%{?dist}
Summary:        Manipulate images with minimal use of memory via ImageMagick
License: MIT
URL: https://github.com/minimagick/minimagick
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/minimagick/minimagick/archive/refs/tags/v5.3.1.tar.gz
Requires: ImageMagick
BuildArch: noarch
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(logger)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A ruby wrapper for ImageMagick command line. Using MiniMagick the ruby
processes memory remains small (it spawns ImageMagick's command line program
mogrify which takes up some memory as well, but is much smaller compared
to RMagick).

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

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
ln -s %{builddir}/spec .
sed -i -e '/require "bundler/ s/^/#/' \
  spec/spec_helper.rb
env -u SOURCE_DATE_EPOCH rspec spec
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-mini_magick-doc -f %{oreon_filedir}/rubygem-mini_magick-doc.list

%changelog

%autochangelog
