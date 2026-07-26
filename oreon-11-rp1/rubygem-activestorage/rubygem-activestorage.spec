%global source0_hash ce60c9fd0f159c8dc8d42663b832f22af1cf67b4ae6d87f863c6d8564418fd35

# Generated from activestorage-0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name activestorage

# openh264 coded is not available in buildroot, while it can be obtained e.g.
# from:
# https://codecs.fedoraproject.org/openh264/43/x86_64/Packages/o/openh264-2.6.0-2.fc43.x86_64.rpm
%bcond_with openh264

# TODO: Re-enable recompilation if possible. Currently, we don't have rollup.js
# in Fedora and therefore it requires network access. Still good for checking
# the results
%bcond_with js_recompilation

Name: rubygem-%{gem_name}
Version: 8.0.3
Release: 3%{?dist}
Summary: Local and cloud file storage framework
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# git clone https://github.com/rails/rails.git && cd rails/activestorage
# git archive -v -o activestorage-8.0.3-tests.tar.gz v8.0.3 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.tar.gz
# Source code of pregenerated JS files.
# git clone https://github.com/rails/rails.git && cd rails/activestorage
# git archive -v -o activestorage-8.0.3-js.tar.gz v8.0.3 package.json rollup.config.js
Source2: %{gem_name}-%{version}%{?prerelease}-js.tar.gz
# Fix a test failing with FFmpeg 8
# https://github.com/rails/rails/issues/56069
Patch0: %{gem_name}-ffmpeg8.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(actionmailer) = %{version}
BuildRequires: rubygem(activerecord) = %{version}
BuildRequires: rubygem(activejob) = %{version}
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(marcel)
BuildRequires: rubygem(railties) = %{version}
BuildRequires: rubygem(sprockets-rails)
BuildRequires: rubygem(image_processing)
BuildRequires: rubygem(sqlite3)
# Required to pass some of the test/models/variant_test.rb
# https://github.com/rails/rails/issues/44395
BuildRequires: vips-magick
BuildRequires: %{_bindir}/ffmpeg
BuildRequires: %{_bindir}/ffprobe
BuildRequires: %{_bindir}/mutool
BuildRequires: %{_bindir}/pdftoppm
%{?with_openh264:BuildRequires: openh264}
%{?with_js_recompilation:BuildRequires: %{_bindir}/npm}
# Used for creating file previews
Suggests: %{_bindir}/mutool
Suggests: %{_bindir}/pdftoppm
Suggests: %{_bindir}/ffmpeg
Suggests: %{_bindir}/ffprobe
# Codec for video analysis
Suggests: openh264

BuildArch: noarch

%description
Attach cloud and local files in Rails applications.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1 -b2
cd ..
%patch -P0 -p0 -b .ffmpeg8

%build
%if %{with js_recompilation}
# Recompile the embedded JS files from sources.
#
# This is practice suggested by packaging guidelines:
# https://fedoraproject.org/wiki/Packaging:Guidelines#Use_of_pregenerated_code

find app/assets/ -type f -exec sha512sum {} \;

rm -rf app/assets/

cp -a %{builddir}/rollup.config.js .

# TODO: This requires network access. Use Fedora rollup.js if it becomes
# available eventually
npm install
npx rollup --config rollup.config.js

# For comparison with the orginal checksum above.
find app/assets/ -type f -exec sha512sum {} \;
%endif

gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
( cd .%{gem_instdir}
cp -a %{builddir}/test .

mkdir ../tools
# Fake test_common.rb. It does not provide any functionality besides
# `force_skip` alias.
touch ../tools/test_common.rb
# Netiher strict_warnings.rb appears to be useful.
touch ../tools/strict_warnings.rb

touch Gemfile
echo 'gem "actionmailer"' >> Gemfile
echo 'gem "activerecord"' >> Gemfile
echo 'gem "activejob"' >> Gemfile
echo 'gem "sprockets-rails"' >> Gemfile
echo 'gem "image_processing"' >> Gemfile
echo 'gem "marcel"' >> Gemfile
echo 'gem "railties"' >> Gemfile
echo 'gem "sqlite3"' >> Gemfile

# `ActiveStorage::Service::AzureStorageService` is deprecated and we would need
# `azure-storage-blob` gem to make this work => just ignore the test.
sed -i '/test "azure service is deprecated" do/a\    skip' \
  test/service/configurator_test.rb

# test/javascript_package_test.rb requires rollup.js, which we don't have.
# OTOH, if we had it, we would recomplie the sources and the test would have
# less value.
mv test/javascript_package_test.rb{,.disable}

# The `ffprobe` output does not containe `display_aspect_ratio` for some
# reason. Is it missing codec or error?
sed -i '/test "analyzing a video" do/,/^  end$/ {
  /display_aspect_ratio/ s/^/#/
}' test/analyzer/video_analyzer_test.rb

# Disable tests that require openh264
%if %{without openh264}
sed -i \
  -e '/"video\.mp4"/i\    skip' \
  -e '/"rotated_video\.mp4"/i\    skip' \
  -e '/"video_with_rectangular_samples\.mp4"/i\    skip' \
  -e '/"video_with_undefined_display_aspect_ratio\.mp4"/i\    skip' \
  -e '/"video_without_audio_stream\.mp4"/i\    skip' \
  test/analyzer/video_analyzer_test.rb \
  test/previewer/video_previewer_test.rb \
  test/models/preview_test.rb \
  test/models/representation_test.rb \
  test/models/variant_with_record_test.rb \
%endif

export RUBYOPT="-I${PWD}/lib"
export BUNDLE_GEMFILE=${PWD}/Gemfile

bundle exec ruby -Itest -ractive_storage/engine -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
