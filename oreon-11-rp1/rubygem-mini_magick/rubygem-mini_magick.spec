%global source0_hash 29395dfd76badcabb6403ee5aff6f681e867074f8f28ce08d78661e9e4a351c4

# Generated from mini_magick-4.8.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mini_magick

Name: rubygem-%{gem_name}
Version: 5.3.1
Release: 3%{?dist}
Summary: Manipulate images with minimal use of memory via ImageMagick
License: MIT
URL: https://github.com/minimagick/minimagick
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone http://github.com/minimagick/minimagick.git --no-checkout && cd minimagick
# git archive -v -o mini_magick-5.3.1-tests.tar.gz v5.3.1 spec/
Source1: %{gem_name}-%{version}-tests.tar.gz

Requires: ImageMagick
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(logger)
BuildRequires: rubygem(rspec)
BuildRequires: ImageMagick
BuildArch: noarch

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

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
( cd .%{gem_instdir}
ln -s %{builddir}/spec .

# avoid Bundler dependency.
sed -i -e '/require "bundler/ s/^/#/' \
  spec/spec_helper.rb

# ImageMagick does not respect MAGICK_TIME_LIMIT when SOURCE_DATE_EPOCH is in
# play
# https://github.com/ImageMagick/ImageMagick/issues/8301
env -u SOURCE_DATE_EPOCH rspec spec
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
%autochangelog
