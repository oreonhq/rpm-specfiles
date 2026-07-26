%global source0_hash 754cc169c9c262980889bec6bfd325ed1dafad34f85242b5a07b60af004742fb

# Generated from image_processing-1.11.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name image_processing

# dhash-vips gem is not in Fedora yet
%bcond_with dhash-vips

Name: rubygem-%{gem_name}
Version: 1.14.0
Release: 3%{?dist}
Summary: High-level wrapper for processing images for the web with ImageMagick or libvips
License: MIT
URL: https://github.com/janko/image_processing
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests are not shipped with the gem, you may check them out like so:
# git clone --no-checkout https://github.com/janko/image_processing
# git archive -v -o image_processing-1.14.0-tests.tar.gz v1.14.0 test/
Source1: %{gem_name}-%{version}-tests.tar.gz
# Disable some test broken by mini_magick 5+.
# https://github.com/janko/image_processing/issues/139
# https://github.com/janko/image_processing/commit/89a162926841733c0df53e7aee95aadf5d28f4c3
Patch0: rubygem-image_processing-1.14.0-Remove-tests-failing-on-newer-IM-versions.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3
BuildRequires: rubygem(minitest) >= 5.8
BuildRequires: rubygem(mini_magick)
%if %{with dhash-vips}
BuildRequires: rubygem(dhash-vips)
%endif
BuildRequires: rubygem(ruby-vips)
BuildArch: noarch

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

%check
( cd .%{gem_instdir}
ln -s %{builddir}/test .

# Tests dependencies that are not needed
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

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/image_processing.gemspec

%changelog
%autochangelog
