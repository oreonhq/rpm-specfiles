%global source0_hash 754cc169c9c262980889bec6bfd325ed1dafad34f85242b5a07b60af004742fb
%global gem_name image_processing
%bcond_with dhash-vips
Name: rubygem-%{gem_name}
Version: 1.14.0
Release:        1%{?dist}
Summary:        High-level wrapper for processing images for the web with ImageMagick or libvips
License: MIT
URL: https://github.com/janko/image_processing
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}-tests.tar.gz
Patch0: rubygem-image_processing-1.14.0-Remove-tests-failing-on-newer-IM-versions.patch
%if %{with dhash-vips}
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(mini_magick)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(ruby-vips)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
High-level wrapper for processing images for the web with ImageMagick or
libvips.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

# dhash-vips is not in Fedora yet.
%if %{without dhash-vips}
%gemspec_remove_dep -d -g dhash-vips
%endif

( cd %{builddir}
%patch 0 -p1
)

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
ln -s %{builddir}/test .
sed -i '/require .minitest.hooks/ s/^/#/g' test/test_helper.rb
sed -i '/require .minispec-metadata/ s/^/#/g' test/test_helper.rb
sed -i '/require .bundler./ s/^/#/' test/test_helper.rb
%if %{without dhash-vips}
sed -i -e '/require .dhash-vips./ s/^/#/g' \
    -e '/^  def distance(image1, image2)/ a \
    skip ' test/test_helper.rb
%endif
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-image_processing-doc -f %{oreon_filedir}/rubygem-image_processing-doc.list

%changelog

%autochangelog
