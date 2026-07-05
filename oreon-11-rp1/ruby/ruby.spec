%global source0_hash none

%global major_version 4
%global minor_version 0
%global teeny_version 1
%global major_minor_version %{major_version}.%{minor_version}

%global ruby_version %{major_minor_version}.%{teeny_version}
%global ruby_release %{ruby_version}

# Specify the named version. It has precedense to revision.
%dnl %global milestone preview2

# Keep the revision enabled for pre-releases from GIT.
%dnl %global revision d428d086c2

%global ruby_archive %{name}-%{ruby_version}

# If revision and milestone are removed/commented out, the official release build is expected.
%if 0%{?milestone:1} != 0
%global ruby_archive %{ruby_archive}-%{?milestone}
%endif

%if 0%{?revision:1} != 0
%global ruby_archive %{ruby_archive}-%{?revision}
%define ruby_archive_timestamp %(stat --printf='@%Y' %{_sourcedir}/%{ruby_archive}.tar.xz | date -f - +"%Y%m%d")
%endif

%if 0%{?milestone:1}%{?revision:1} != 0
%define development_release ~%{?ruby_archive_timestamp}%{?milestone}%{?!milestone:%{?revision:git%{revision}}}
%endif


# The RubyGems library has to stay out of Ruby directory tree, since the
# RubyGems should be share by all Ruby implementations.
%global rubygems_dir %{_datadir}/rubygems

## BUNDLED_GEMS_VERSIONS

# Bundled libraries versions
%global rubygems_version 4.0.3
%global rubygems_molinillo_version 0.8.0
%global rubygems_net_http_version 0.7.0
%global rubygems_net_protocol_version 0.2.2
%global rubygems_optparse_version 0.8.0
%global rubygems_resolv_version 0.6.2
%global rubygems_securerandom_version 0.4.1
%global rubygems_timeout_version 0.4.4
%global rubygems_tsort_version 0.2.0
%global rubygems_uri_version 1.1.1

# Default gems.
%global bundler_version 4.0.3
%global bundler_connection_pool_version 2.5.4
%global bundler_fileutils_version 1.8.0
%global bundler_net_http_persistent_version 4.0.6
%global bundler_pub_grub_version 0.5.0
%global bundler_securerandom_version 0.4.1
%global bundler_thor_version 1.4.0
%global bundler_tsort_version 0.2.0
%global bundler_uri_version 1.1.1

%global date_version 3.5.1
%global delegate_version 0.6.1
%global did_you_mean_version 2.0.0
%global digest_version 3.2.1
%global english_version 0.8.1
%global erb_version 6.0.1
%global error_highlight_version 0.7.1
%global etc_version 1.4.6
%global fcntl_version 1.3.0
%global fileutils_version 1.8.0
%global find_version 0.2.0
%global forwardable_version 1.4.0
%global io_console_version 0.8.2
%global io_nonblock_version 0.3.2
%global io_wait_version 0.4.0
%global ipaddr_version 1.2.8
%global json_version 2.18.0
%global net_http_version 0.9.1
%global net_protocol_version 0.2.2
%global open_uri_version 0.5.0
%global open3_version 0.2.1
%global openssl_version 4.0.0
%global optparse_version 0.8.1
%global pp_version 0.6.3
%global prettyprint_version 0.2.0
%global prism_version 1.8.0
%global psych_version 5.3.1
%global resolv_version 0.7.0
%global ruby2_keywords_version 0.0.5
%global securerandom_version 0.4.1
%global shellwords_version 0.2.2
%global singleton_version 0.3.0
%global stringio_version 3.2.0
%global strscan_version 3.1.6
%global syntax_suggest_version 2.0.2
%global tempfile_version 0.3.1
%global time_version 0.4.2
%global timeout_version 0.6.0
%global tmpdir_version 0.3.1
%global tsort_version 0.2.0
%global un_version 0.3.0
%global uri_version 1.1.1
%global weakref_version 0.1.4
%global win32_registry_version 0.1.2
%global yaml_version 0.4.0
%global zlib_version 3.2.2

# Bundled gems.
%global abbrev_version 0.1.2
%global base64_version 0.3.0
%global benchmark_version 0.5.0
%global bigdecimal_version 4.0.1
%global csv_version 3.3.5
%global debug_version 1.11.1
%global drb_version 2.2.3
%global fiddle_version 1.1.8
%global getoptlong_version 0.2.1
%global irb_version 1.16.0
%global logger_version 1.7.0
%global matrix_version 0.4.3
%global minitest_version 6.0.0
%global mutex_m_version 0.3.0
%global net_ftp_version 0.3.9
%global net_imap_version 0.6.2
%global net_pop_version 0.1.2
%global net_smtp_version 0.5.1
%global nkf_version 0.2.0
%global observer_version 0.1.2
%global ostruct_version 0.6.3
%global power_assert_version 3.0.1
%global prime_version 0.1.4
%global pstore_version 0.2.0
%global racc_version 1.8.1
%global rake_version 13.3.1
%global rbs_version 3.10.0
%global rdoc_version 7.0.3
%global readline_version 0.0.4
%global reline_version 0.6.3
%global repl_type_completor_version 0.1.12
%global resolv_replace_version 0.1.1
%global rexml_version 3.4.4
%global rinda_version 0.2.0
%global rss_version 0.3.2
%global syslog_version 0.3.0
%global test_unit_version 3.7.5
%global typeprof_version 0.31.1
%global win32ole_version 1.9.2

## END_BUNDLED_GEMS_VERSIONS

# Bundled nkf version
%global bundled_nkf_version 2.1.5

%global tapset_libdir %(echo %{_libdir} | sed 's/64//')*

%if 0%{?fedora} >= 19
%bcond_without rubypick
%endif

%bcond_without cmake
%bcond_without git
%bcond_without gmp
%bcond_without hostname
%bcond_without systemtap
%bcond_without rust

# Don't build rust parts if we are not building with rust bits.
%if 0%{?with_rust}
# YJIT and ZJIT is supported on x86_64 and aarch64.
# https://github.com/ruby/ruby/blob/master/doc/jit/yjit.md
# https://github.com/ruby/ruby/blob/master/doc/jit/zjit.md
%ifarch x86_64 aarch64
%bcond_without yjit
%bcond_without zjit
%endif
%endif

# Enable test when building on local.
%bcond_with bundler_tests
%bcond_without parallel_tests

%if 0%{?fedora}
%bcond_without hardening_test
%endif

# The additional linker flags break binary rubygem- packages.
# https://bugzilla.redhat.com/show_bug.cgi?id=2043092
%undefine _package_note_flags

Summary: An interpreter of object-oriented scripting language
Name: ruby
Version: %{ruby_version}%{?development_release}
Release: 33%{?dist}
# Licenses, which are likely not included in binary RPMs:
# Apache-2.0:
#   benchmark/gc/redblack.rb
#     But this file might be BSD-2-Clause licensed after all:
#     https://bugs.ruby-lang.org/issues/20420
# GPL-1.0-or-later: ext/win32/lib/win32/sspi.rb
# GPL-1.0-or-later OR Artistic-1.0-Perl: win32/win32.c, include/ruby/win32.h,
#   ext/win32ole/win32ole.c
# IETF (this is not official SPDX identifier)
#   .bundle/gems/net-imap-0.4.9/LICENSE.txt
#     Licenses in this file covers fair use and don't need to be listed:
#     https://gitlab.com/fedora/legal/fedora-license-data/-/issues/506
#
# BSD-3-Clause: missing/{crypt,mt19937,setproctitle}.c, addr2line.c:2652
# CC0: ccan/{build_assert/build_assert.h,check_type/check_type.h,
#   container_of/container_of.h,str/str.h}
#   Allowed based on 'grandfather clause':
#   https://gitlab.com/fedora/legal/fedora-license-data/-/blob/7d9720b2cfd8ccb98d1975312942d99588a0da7c/data/CC0-1.0.toml#L11-14
#   https://gitlab.com/fedora/legal/fedora-license-data/-/issues/499
# dtoa: missing/dtoa.c
# GPL-3.0-or-later WITH Bison-exception-2.2: parse.{c,h}, ext/ripper/ripper.c
# HPND-Markus-Kuhn: missing/langinfo.c
# ISC: missing/strl{cat,cpy}.c
# LicenseRef-Fedora-Public-Domain: include/ruby/st.h, strftime.c, missing/*, ...
#   https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/145
# MIT: ccan/list/list.h
# Ruby OR BSD-2-Clause OR GPL-1.0-or-later: lib/net/protocol.rb
# Ruby-pty: ext/pty/pty.c
# Unicode-DFS-2015: some of enc/trans/**/*.src
#   There is also license review ticket here:
#   https://gitlab.com/fedora/legal/fedora-license-data/-/issues/500
# zlib: ext/digest/md5/md5.*, ext/nkf/nkf-utf8/nkf.c
License: (Ruby OR BSD-2-Clause) AND (Ruby OR BSD-2-Clause OR GPL-1.0-or-later) AND BSD-3-Clause AND (GPL-3.0-or-later WITH Bison-exception-2.2) AND ISC AND LicenseRef-Fedora-Public-Domain AND MIT AND CC0-1.0 AND zlib AND Unicode-DFS-2015 AND HPND-Markus-Kuhn AND Ruby-pty
URL: https://www.ruby-lang.org/
Source0:        https://cache.ruby-lang.org/pub/%{name}/%{major_minor_version}/%{ruby_archive}.tar.xz
Source1: operating_system.rb
# TODO: Try to push SystemTap support upstream.
Source2: libruby.stp
Source3: ruby-exercise.stp
Source4: macros.ruby
Source5: macros.rubygems
# RPM dependency generators.
Source6: rubygems.attr
Source7: rubygems.req
Source8: rubygems.prov
Source9: rubygems.con
# ABRT hoook test case.
Source10: test_abrt.rb
# SystemTap tests.
Source11: test_systemtap.rb
# Ruby OpenSSL FIPS tests.
Source12: test_openssl_fips.rb
# RPM gem Requires dependency generator tests.
Source13: rpm_test_helper.rb
Source14: test_rubygems_req.rb
Source15: test_rubygems_prov.rb
Source16: test_rubygems_con.rb

# The load directive is supported since RPM 4.12, i.e. F21+. The build process
# fails on older Fedoras.
%{load:%{SOURCE4}}
%{load:%{SOURCE5}}

%define _local_file_attrs local_generator
%define __local_generator_requires make -C %{_builddir}/%{buildsubdir}/%{_vpath_builddir} -s runruby TESTRUN_SCRIPT="--enable-gems %{SOURCE7}"
%define __local_generator_provides make -C %{_builddir}/%{buildsubdir}/%{_vpath_builddir} -s runruby TESTRUN_SCRIPT="--enable-gems %{SOURCE8}"
%define __local_generator_conflicts make -C %{_builddir}/%{buildsubdir}/%{_vpath_builddir} -s runruby TESTRUN_SCRIPT="--enable-gems %{SOURCE9}"
%define __local_generator_path ^%{gem_dir}/specifications/.*\.gemspec$

# Fix ruby_version abuse.
# https://bugs.ruby-lang.org/issues/11002
Patch0: ruby-2.3.0-ruby_version.patch
# Fix ruby_version abuse for rdoc.
# Since rdoc is bundled gem, the patch is split from ruby-2.3.0-ruby_version.patch
# re-made in ruby/rdoc git source and will be applied in correct path in the
# specfile where we have the exact rdoc version that is part of the path.
Patch1: ruby-2.3.0-ruby_version-Add-ruby_version_dir_name-support-for-RDoc.patch
# http://bugs.ruby-lang.org/issues/7807
Patch2: ruby-2.1.0-Prevent-duplicated-paths-when-empty-version-string-i.patch
# Allows to override libruby.so placement. Hopefully we will be able to return
# to plain --with-rubyarchprefix.
# http://bugs.ruby-lang.org/issues/8973
Patch3: ruby-2.1.0-Enable-configuration-of-archlibdir.patch
# Force multiarch directories for i.86 to be always named i386. This solves
# some differencies in build between Fedora and RHEL.
Patch4: ruby-2.1.0-always-use-i386.patch
# Allows to install RubyGems into custom directory, outside of Ruby's tree.
# http://bugs.ruby-lang.org/issues/5617
Patch5: ruby-2.1.0-custom-rubygems-location.patch
# The ABRT hook used to be initialized by preludes via following patches:
# https://bugs.ruby-lang.org/issues/8566
# https://bugs.ruby-lang.org/issues/15306
# Unfortunately, due to https://bugs.ruby-lang.org/issues/16254
# and especially since https://github.com/ruby/ruby/pull/2735
# this would require boostrapping:
# https://lists.fedoraproject.org/archives/list/ruby-sig@lists.fedoraproject.org/message/LH6L6YJOYQT4Y5ZNOO4SLIPTUWZ5V45Q/
# For now, load the ABRT hook via this simple patch:
Patch6: ruby-2.7.0-Initialize-ABRT-hook.patch
# Disable syntax_suggest test suite, which tries to download its dependencies.
# https://bugs.ruby-lang.org/issues/19297
Patch7: ruby-3.3.0-Disable-syntax-suggest-test-case.patch
# Add a way to provide %%build_rustflags to JIT's rustc.
# https://github.com/ruby/ruby/pull/15695
Patch8: ruby-4.0.1-Support-customizable-rustc_flags-for-rustc-builds.patch
# https://github.com/ruby/rdoc/pull/1531
# Fix error with `gem install --document=rdoc,ri`
Patch9: rdoc-pr1531-fix-mutilple-document-installation.patch

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%{?with_rubypick:Requires: rubypick}
Recommends: ruby(rubygems) >= %{rubygems_version}
Recommends: ruby-default-gems >= %{version}-%{release}
Recommends: ruby-bundled-gems >= %{version}-%{release}
Recommends: rubygem(bigdecimal) >= %{bigdecimal_version}

# Build dependencies
BuildRequires: autoconf
BuildRequires: gcc
BuildRequires: make
BuildRequires: libffi-devel
BuildRequires: libxcrypt-devel
BuildRequires: libyaml-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel
%{?with_gmp:BuildRequires: gmp-devel}
%{?with_systemtap:BuildRequires: %{_bindir}/dtrace}
%{?with_systemtap:BuildRequires: systemtap-sdt-devel}
%if 0%{?with_rust}
BuildRequires: %{_bindir}/rustc

# We need the %%{build_rustflags}, EL needs different package than Fedora.
%if 0%{?fedora}
BuildRequires: rust-srpm-macros
%else
Buildrequires: rust-toolset
%endif

%endif

# Install section
BuildRequires: multilib-rpm-config

# Check dependencies

# Required to test hardening.
%{?with_hardening_test:BuildRequires: %{_bindir}/checksec}

# Needed to pass test_set_program_name(TestRubyOptions)
BuildRequires: procps
# Neede by `Socket.gethostname returns the host name ERROR`
%{?with_hostname:BuildRequires: %{_bindir}/hostname}

# RubyGems test suite optional dependencies.
%{?with_git:BuildRequires: git}
# `cmake` is required for test/rubygems/test_gem_ext_cmake_builder.rb.
%{?with_cmake:BuildRequires: %{_bindir}/cmake}

# The bundler/spec/runtime/setup_spec.rb requires the command `man`.
%{?with_bundler_tests:BuildRequires: %{_bindir}/man}


# This package provides %%{_bindir}/ruby-mri therefore it is marked by this
# virtual provide. It can be installed as dependency of rubypick.
Provides: ruby(runtime_executable) = %{ruby_release}

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.


%package devel
Summary:    A Ruby development environment
Requires:   %{name}%{?_isa} = %{version}-%{release}
# This would not be needed if ~50 packages depending on -devel used
# --disable-gems
Requires:   rubygems
# Users need CFLAGS from /usr/lib/rpm/redhat/redhat-hardened-cc1
# for building gems with binary extensions (rhbz#1905222).
Recommends: redhat-rpm-config

%description devel
Header files and libraries for building an extension library for the
Ruby or an application embedding Ruby.

%package libs
Summary:    Libraries necessary to run Ruby
Provides:   ruby(release) = %{ruby_release}

# Virtual provides for CCAN copylibs.
# https://fedorahosted.org/fpc/ticket/364
Provides: bundled(ccan-build_assert)
Provides: bundled(ccan-check_type)
Provides: bundled(ccan-container_of)
Provides: bundled(ccan-list)

# StdLib default gems.
Provides: bundled(rubygem-did_you_mean) = %{did_you_mean_version}
Provides: bundled(rubygem-openssl) = %{openssl_version}


%description libs
This package includes the libruby, necessary to run Ruby.


# TODO: Rename or not rename to ruby-rubygems?
%package -n rubygems
Summary:    The Ruby standard for packaging ruby libraries
Version:    %{rubygems_version}
# BSD-2-Clause OR Ruby:
#   lib/rubygems/net-http/
#   lib/rubygems/net-protocol/
#   lib/rubygems/optparse/
#   lib/rubygems/resolv/
#   lib/rubygems/timeout/
#   lib/rubygems/tsort/
# MIT: lib/rubygems/resolver/molinillo
# Ruby OR BSD-2-Clause OR GPL-1.0-or-later: lib/net/protocol.rb
License:    (Ruby OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Ruby) AND (Ruby OR BSD-2-Clause OR GPL-1.0-or-later) AND MIT
Requires:   ruby(release)
Recommends: rubygem(bundler) >= %{bundler_version}
Recommends: rubygem(rdoc) >= %{rdoc_version}
Recommends: rubygem(io-console)
Requires:   rubygem(psych) >= %{psych_version}%{?psych_prerelease:~%{sub %{psych_prerelease} 2 -1}}
Provides:   gem = %{version}-%{release}
Provides:   ruby(rubygems) = %{version}-%{release}
Provides:   bundled(rubygems) = %{rubygems_version}
# https://github.com/rubygems/rubygems/pull/1189#issuecomment-121600910
Provides:   bundled(rubygem-molinillo) = %{rubygems_molinillo_version}
Provides:   bundled(rubygem-net-http) = %{rubygems_net_http_version}
Provides:   bundled(rubygem-net-protocol) = %{rubygems_net_protocol_version}
Provides:   bundled(rubygem-optparse) = %{rubygems_optparse_version}
Provides:   bundled(rubygem-resolv) = %{rubygems_resolv_version}
Provides:   bundled(rubygem-securerandom) = %{rubygems_securerandom_version}
Provides:   bundled(rubygem-timeout) = %{rubygems_timeout_version}
Provides:   bundled(rubygem-tsort) = %{rubygems_tsort_version}
Provides:   bundled(rubygem-uri) = %{rubygems_uri_version}

BuildArch:  noarch

%description -n rubygems
RubyGems is the Ruby standard for publishing and managing third party
libraries.


%package -n rubygems-devel
Summary:    Macros and development tools for packaging RubyGems
Version:    %{rubygems_version}
License:    MIT
Requires:   ruby(rubygems) >= %{version}-%{release}
# Needed for RDoc documentation format generation.
Requires:   rubygem(json) >= %{json_version}
Requires:   rubygem(rdoc) >= %{rdoc_version}
BuildArch:  noarch

%description -n rubygems-devel
Macros and development tools for packaging RubyGems.


# Default gems
#
# These packages are part of Ruby StdLib and are expected to be loadable even
# with disabled RubyGems.

%package default-gems
Summary:    Default gems which are part of Ruby StdLib
Supplements: ruby(rubygems)
# Obsoleted by Ruby 3.0 in F34 timeframe.
Obsoletes: rubygem-openssl < 2.2.0-145
BuildArch:  noarch

%description default-gems
The .gemspec files and executables of default gems, which are part of Ruby
StdLib.


%package -n rubygem-irb
Summary:    The Interactive Ruby
Version:    %{irb_version}
License:    Ruby OR BSD-2-Clause
Provides:   irb = %{version}-%{release}
Provides:   bundled(rubygem-irb) = %{irb_version}
BuildArch:  noarch

%description -n rubygem-irb
The irb is acronym for Interactive Ruby.  It evaluates ruby expression
from the terminal.


%package -n rubygem-rdoc
Summary:    A tool to generate HTML and command-line documentation for Ruby projects
Version:    %{rdoc_version}
# BSD-3-Clause: lib/rdoc/generator/darkfish.rb
# CC-BY-2.5: lib/rdoc/generator/template/darkfish/images/loadingAnimation.gif
# OFL-1.1-RFN: lib/rdoc/generator/template/darkfish/css/fonts.css
# MIT: lib/rdoc/generator/aliki.rb
# MIT: lib/rdoc/generator/template/aliki/*
# Note that RDoc now embeds Racc parser:
# https://github.com/ruby/rdoc/pull/1019
# Luckily, this should have no license impact:
# https://github.com/ruby/racc/blob/5eb07b28bfb3e193a1cac07798fe7be7e1e246c4/lib/racc/parser.rb#L8-L10
License:    GPL-2.0-only AND Ruby AND BSD-3-Clause AND CC-BY-2.5 AND OFL-1.1-RFN AND MIT
Requires:   rubygem(io-console)
Requires:   rubygem(json) >= %{json_version}
Provides:   rdoc = %{version}-%{release}
Provides:   ri = %{version}-%{release}
Provides:   bundled(rubygem-rdoc) = %{rdoc_version}
BuildArch:  noarch

%description -n rubygem-rdoc
RDoc produces HTML and command-line documentation for Ruby projects.  RDoc
includes the 'rdoc' and 'ri' tools for generating and displaying online
documentation.


%package doc
Summary:    Documentation for %{name}
Requires:   %{_bindir}/ri
BuildArch:  noarch

%description doc
This package contains documentation for %{name}.


%package -n rubygem-bigdecimal
Summary:    BigDecimal provides arbitrary-precision floating point decimal arithmetic
Version:    %{bigdecimal_version}
# dtoa: missing/dtoa.c
License:    (Ruby OR BSD-2-Clause) AND dtoa
Provides:   bundled(rubygem-bigdecimal) = %{bigdecimal_version}

%description -n rubygem-bigdecimal
Ruby provides built-in support for arbitrary precision integer arithmetic.
For example:

42**13 -> 1265437718438866624512

BigDecimal provides similar support for very large or very accurate floating
point numbers. Decimal arithmetic is also useful for general calculation,
because it provides the correct answers people expect–whereas normal binary
floating point arithmetic often introduces subtle errors because of the
conversion between base 10 and base 2.


%package -n rubygem-io-console
Summary:    IO/Console is a simple console utilizing library
Version:    %{io_console_version}
License:    Ruby OR BSD-2-Clause
Provides:   bundled(rubygem-io-console) = %{io_console_version}

%description -n rubygem-io-console
IO/Console provides very simple and portable access to console. It doesn't
provide higher layer features, such like curses and readline.


%package -n rubygem-json
Summary:    This is a JSON implementation as a Ruby extension in C
Version:    %{json_version}
# Apache-2.0 OR BSL-1.0: ext/json/vendor/ryu.h
# MIT: ext/json/vendor/jeaiii-ltoa.h
# BSL-1.0: ext/json/vendor/fpconv.c
License:    (Ruby OR BSD-2-Clause) AND (Apache-2.0 OR BSL-1.0) AND MIT AND BSL-1.0
Provides:   bundled(rubygem-json) = %{json_version}
# https://github.com/ulfjack/ryu
Provides:   bundled(ryu)
# jeaiii-ltoa.h
# https://github.com/jeaiii/itoa
Provides:   bundled(itoa)
# https://github.com/night-shift/fpconv
Provides:   bundled(fpconv)

%description -n rubygem-json
This is a implementation of the JSON specification according to RFC 4627.
You can think of it as a low fat alternative to XML, if you want to store
data to disk or transmit it over a network rather than use a verbose
markup language.


%package -n rubygem-psych
Summary:    A libyaml wrapper for Ruby
Version:    %{psych_version}%{?psych_prerelease:~%{sub %{psych_prerelease} 2 -1}}
License:    MIT
Provides:   bundled(rubygem-psych) = %{psych_version}%{?psych_prerelease:~%{sub %{psych_prerelease} 2 -1}}

%description -n rubygem-psych
Psych is a YAML parser and emitter. Psych leverages
libyaml[http://pyyaml.org/wiki/LibYAML] for its YAML parsing and emitting
capabilities. In addition to wrapping libyaml, Psych also knows how to
serialize and de-serialize most Ruby objects to and from the YAML format.


%package -n rubygem-bundler
Summary:    Library and utilities to manage a Ruby application's gem dependencies
Version:    %{bundler_version}
# BSD-2-Clause OR Ruby:
#   lib/bundler/vendor/fileutils
#   lib/bundler/vendor/tsort
#   lib/bundler/vendor/uri
# MIT:
#   lib/bundler/vendor/connection_pool
#   lib/bundler/vendor/net-http-persistent
#   lib/bundler/vendor/pub_brub
#   lib/bundler/vendor/thor
#   lib/rubygems/resolver/molinillo
License:    MIT AND (Ruby OR BSD-2-Clause)
Requires:   rubygem(io-console)
Provides:   bundled(rubygem-bundler) = %{bundler_version}
# https://github.com/bundler/bundler/issues/3647
Provides:   bundled(rubygem-connection_pool) = %{bundler_connection_pool_version}
Provides:   bundled(rubygem-fileutils) = %{bundler_fileutils_version}
Provides:   bundled(rubygem-net-http-persistent) = %{bundler_net_http_persistent_version}
Provides:   bundled(rubygem-pub_grub) = %{bundler_pub_grub_version}
Provides:   bundled(rubygem-securerandom) = %{bundler_securerandom_version}
Provides:   bundled(rubygem-thor) = %{bundler_thor_version}
Provides:   bundled(rubygem-tsort) = %{bundler_tsort_version}
Provides:   bundled(rubygem-uri) = %{bundler_uri_version}
BuildArch:  noarch

%description -n rubygem-bundler
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably.


# Bundled gems
#
# These are regular packages, which might be installed just optionally. Users
# should list them among their dependencies (in Gemfile).

%package bundled-gems
Summary:    Bundled gems which are part of Ruby StdLib
Provides:   bundled(rubygem-abbrev) = %{abbrev_version}
Provides:   bundled(rubygem-base64) = %{base64_version}
Provides:   bundled(rubygem-benchmark) = %{benchmark_version}
Provides:   bundled(rubygem-csv) = %{csv_version}
Provides:   bundled(rubygem-debug) = %{debug_version}
Provides:   bundled(rubygem-drb) = %{drb_version}
Provides:   bundled(rubygem-getoptlong) = %{getoptlong_version}
Provides:   bundled(rubygem-fiddle) = %{fiddle_version}
Provides:   bundled(rubygem-logger) = %{logger_version}
Provides:   bundled(rubygem-matrix) = %{matrix_version}
Provides:   bundled(rubygem-mutex_m) = %{mutex_m_version}
Provides:   bundled(rubygem-net-ftp) = %{net_ftp_version}
Provides:   bundled(rubygem-net-imap) = %{net_imap_version}
Provides:   bundled(rubygem-net-pop) = %{net_pop_version}
Provides:   bundled(rubygem-net-smtp) = %{net_smtp_version}
Provides:   bundled(rubygem-nkf) = %{nkf_version}
Provides:   bundled(rubygem-observer) = %{observer_version}
Provides:   bundled(rubygem-ostruct) = %{ostruct_version}
Provides:   bundled(rubygem-prime) = %{prime_version}
Provides:   bundled(rubygem-pstore) = %{pstore_version}
Provides:   bundled(rubygem-readline) = %{readline_version}
Provides:   bundled(rubygem-reline) = %{reline_version}
Provides:   bundled(rubygem-repl_type_completor) = %{repl_type_completor_version}
Provides:   bundled(rubygem-resolv-replace) = %{resolv_replace_version}
Provides:   bundled(rubygem-rinda) = %{rinda_version}
Provides:   bundled(rubygem-syslog) = %{syslog_version}
# https://github.com/nurse/nkf
# Please note that nkf going to be promoted to bundled gem in Ruby 3.4:
# https://github.com/ruby/ruby/commit/2e3a7f70ae71650be6ea38a483f66ce17ca5eb1d
Provides:   bundled(nkf) = %{bundled_nkf_version}


%description bundled-gems
Bundled gems which are part of Ruby StdLib. While being part of Ruby, these
needs to be listed in Gemfile to be used by Bundler.


%package -n rubygem-minitest
Summary:    Minitest provides a complete suite of testing facilities
Version:    %{minitest_version}
License:    MIT
Provides:   bundled(rubygem-minitest) = %{minitest_version}
BuildArch:  noarch

%description -n rubygem-minitest
minitest/test is a small and incredibly fast unit testing framework.

minitest/spec is a functionally complete spec engine.

minitest/benchmark is an awesome way to assert the performance of your
algorithms in a repeatable manner.

minitest/pride shows pride in testing and adds coloring to your test
output.


%package -n rubygem-power_assert
Summary:    Power Assert for Ruby
Version:    %{power_assert_version}
License:    Ruby OR BSD-2-Clause
Provides:   bundled(rubygem-power_assert) = %{power_assert_version}
BuildArch:  noarch

%description -n rubygem-power_assert
Power Assert shows each value of variables and method calls in the expression.
It is useful for testing, providing which value wasn't correct when the
condition is not satisfied.


%package -n rubygem-rake
Summary:    Ruby based make-like utility
Version:    %{rake_version}
License:    MIT
Provides:   rake = %{version}-%{release}
Provides:   bundled(rubygem-rake) = %{rake_version}
BuildArch:  noarch

%description -n rubygem-rake
Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.


%package -n rubygem-rbs
Summary:    Type signature for Ruby
Version:    %{rbs_version}
License:    Ruby OR BSD-2-Clause
Provides:   bundled(rubygem-rbs) = %{rbs_version}

%description -n rubygem-rbs
RBS is the language for type signatures for Ruby and standard library
definitions.


%package -n rubygem-test-unit
Summary:    An xUnit family unit testing framework for Ruby
Version:    %{test_unit_version}
# lib/test/unit/diff.rb is a double license of the Ruby license and PSF license.
License:    (Ruby OR BSD-2-Clause) AND (Ruby OR BSD-2-Clause OR Python-2.0.1)
Provides:   bundled(rubygem-test-unit) = %{test_unit_version}
BuildArch:  noarch

%description -n rubygem-test-unit
Test::Unit (test-unit) is unit testing framework for Ruby, based on xUnit
principles. These were originally designed by Kent Beck, creator of extreme
programming software development methodology, for Smalltalk's SUnit. It allows
writing tests, checking results and automated testing in Ruby.


%package -n rubygem-racc
Version:    %{racc_version}
Summary:    Racc is a LALR(1) parser generator
License:    Ruby OR BSD-2-Clause
URL:        https://github.com/ruby/racc
Provides:   bundled(rubygem-racc) = %{racc_version}

%description -n rubygem-racc
Racc is a LALR(1) parser generator.
It is written in Ruby itself, and generates Ruby program.


%package -n rubygem-rexml
Summary:    An XML toolkit for Ruby
Version:    %{rexml_version}
License:    BSD-2-Clause
URL:        https://github.com/ruby/rexml
Provides:   bundled(rubygem-rexml) = %{rexml_version}
BuildArch:  noarch

%description -n rubygem-rexml
REXML was inspired by the Electric XML library for Java, which features an
easy-to-use API, small size, and speed. Hopefully, REXML, designed with the same
philosophy, has these same features. I've tried to keep the API as intuitive as
possible, and have followed the Ruby methodology for method naming and code
flow, rather than mirroring the Java API.

REXML supports both tree and stream document parsing. Stream parsing is faster
(about 1.5 times as fast). However, with stream parsing, you don't get access to
features such as XPath.


%package -n rubygem-rss
Summary:    Family of libraries that support various formats of XML "feeds"
Version:    %{rss_version}
License:    BSD-2-Clause
URL:        https://github.com/ruby/rss
Provides:   bundled(rubygem-rss) = %{rss_version}
BuildArch:  noarch

%description -n rubygem-rss
Really Simple Syndication (RSS) is a family of formats that describe 'feeds',
specially constructed XML documents that allow an interested person to subscribe
and receive updates from a particular web service. This library provides tooling
to read and create these feeds.


%package -n rubygem-typeprof
Summary:    TypeProf is a type analysis tool for Ruby code based on abstract interpretation
Version:    %{typeprof_version}
License:    MIT
URL:        https://github.com/ruby/typeprof
Provides:   bundled(rubygem-typeprof) = %{typeprof_version}
BuildArch:  noarch

%description -n rubygem-typeprof
TypeProf performs a type analysis of non-annotated Ruby code.
It abstractly executes input Ruby code in a level of types instead of values,
gathers what types are passed to and returned by methods, and prints the
analysis result in RBS format, a standard type description format for Ruby
3.0.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{ruby_archive}

%patch 0 -p1

pushd .bundle/gems/rdoc-%{rdoc_version}
%patch 1 -p1
%patch 9 -p1
popd

%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
%patch 5 -p1
%patch 6 -p1
%patch 7 -p1
%patch 8 -p1

# Provide an example of usage of the tapset:
cp -a %{SOURCE3} .

%build
autoconf

%global _configure %{_builddir}/%{buildsubdir}/configure

mkdir -p %{_vpath_builddir}
pushd %{_vpath_builddir}

%configure \
        --with-rubylibprefix='%{ruby_libdir}' \
        --with-archlibdir='%{_libdir}' \
        --with-rubyarchprefix='%{ruby_libarchdir}' \
        --with-sitedir='%{ruby_sitelibdir}' \
        --with-sitearchdir='%{ruby_sitearchdir}' \
        --with-vendordir='%{ruby_vendorlibdir}' \
        --with-vendorarchdir='%{ruby_vendorarchdir}' \
        --with-rubyhdrdir='%{_includedir}' \
        --with-rubyarchhdrdir='%{_includedir}' \
        --with-sitearchhdrdir='$(sitehdrdir)/$(arch)' \
        --with-vendorarchhdrdir='$(vendorhdrdir)/$(arch)' \
        --with-rubygemsdir='%{rubygems_dir}' \
        --with-ruby-pc='%{name}.pc' \
        --with-compress-debug-sections=no \
        --disable-rpath \
        --enable-mkmf-verbose \
        --enable-shared \
        --with-ruby-version='' \
        --enable-multiarch \
        %{?with_yjit: --enable-yjit} \
        %{?with_zjit: --enable-zjit} \
        %{?with_rust: rustc_flags='%{build_rustflags}'} \

popd

# V=1 in %%make_build outputs the compiler options more verbosely.
# https://bugs.ruby-lang.org/issues/18756
%make_build COPY="cp -p" -C %{_vpath_builddir}

%install
rm -rf %{buildroot}

%make_install -C %{_vpath_builddir}

# TODO: Regenerate RBS parser in lib/rbs/parser.rb

# Rename ruby/config.h to ruby/config-<arch>.h to avoid file conflicts on
# multilib systems and install config.h wrapper
%multilib_fix_c_header --file %{_includedir}/%{name}/config.h

# `ruby` executable is placed in some strange directory for some unknow
# reasons.
# https://bugs.ruby-lang.org/issues/20800
# https://github.com/ruby/ruby/pull/12043
CONFIG_TARGET_DIR=%{buildroot}%{_exec_prefix}/$( \
  %{_vpath_builddir}/miniruby -I%{_vpath_builddir} -rrbconfig -e 'puts RbConfig::CONFIG["config_target"]'
)
mv ${CONFIG_TARGET_DIR}/bin/ruby %{buildroot}%{_bindir}
rm -rd ${CONFIG_TARGET_DIR}

# Rename the ruby executable. It is replaced by RubyPick.
%{?with_rubypick:mv %{buildroot}%{_bindir}/%{name}{,-mri}}

# Kill bundled certificates, as they should be part of ca-certificates.
for cert in \
  rubygems.org/GlobalSign.pem
do
  rm %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/$cert
  rm -d $(dirname %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/$cert) || :
done
# Ensure there is not forgotten any certificate.
test ! "$(ls -A %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/ 2>/dev/null)"

# Move macros file into proper place and replace the %%{name} macro, since it
# would be wrongly evaluated during build of other packages.
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE4} %{buildroot}%{_rpmmacrodir}/macros.ruby
sed -i "s/%%{name}/%{name}/" %{buildroot}%{_rpmmacrodir}/macros.ruby
install -m 644 %{SOURCE5} %{buildroot}%{_rpmmacrodir}/macros.rubygems
sed -i "s/%%{name}/%{name}/" %{buildroot}%{_rpmmacrodir}/macros.rubygems

# Install dependency generators.
mkdir -p %{buildroot}%{_fileattrsdir}
install -m 644 %{SOURCE6} %{buildroot}%{_fileattrsdir}
install -m 755 %{SOURCE7} %{buildroot}%{_rpmconfigdir}
install -m 755 %{SOURCE8} %{buildroot}%{_rpmconfigdir}
install -m 755 %{SOURCE9} %{buildroot}%{_rpmconfigdir}

# Install custom operating_system.rb.
mkdir -p %{buildroot}%{rubygems_dir}/rubygems/defaults
cp %{SOURCE1} %{buildroot}%{rubygems_dir}/rubygems/defaults

# Move gems root into common direcotry, out of Ruby directory structure.
mv %{buildroot}%{ruby_libdir}/gems %{buildroot}%{gem_dir}

# Create folders for gem binary extensions.
# TODO: These folders should go into rubygem-filesystem but how to achieve it,
# since noarch package cannot provide arch dependent subpackages?
# http://rpm.org/ticket/78
mkdir -p %{buildroot}%{_exec_prefix}/lib{,64}/gems/%{name}

# Move bundled rubygems to %%gem_dir and %%gem_extdir_mri
# make symlinks for io-console, which is considered to be part of stdlib by other Gems
# TODO: Put help files into proper location.
# https://bugs.ruby-lang.org/issues/15359
mkdir -p %{buildroot}%{gem_libdir bundler}
mv %{buildroot}%{ruby_libdir}/bundler.rb %{buildroot}%{gem_libdir bundler}
mv %{buildroot}%{ruby_libdir}/bundler %{buildroot}%{gem_libdir bundler}
mv %{buildroot}%{gem_spec -d bundler} %{buildroot}%{gem_spec bundler}

mkdir -p %{buildroot}%{gem_libdir io-console}
mkdir -p %{buildroot}%{gem_extdir_mri io-console}/io
mv %{buildroot}%{ruby_libdir}/io %{buildroot}%{gem_libdir io-console}
mv %{buildroot}%{ruby_libarchdir}/io/console.so %{buildroot}%{gem_extdir_mri io-console}/io
touch %{buildroot}%{gem_extdir_mri io-console}/gem.build_complete
mv %{buildroot}%{gem_spec -d io-console} %{buildroot}%{gem_spec io-console}
ln -s %{gem_libdir io-console}/io %{buildroot}%{ruby_libdir}/io
ln -s %{gem_extdir_mri io-console}/io/console.so %{buildroot}%{ruby_libarchdir}/io/console.so

mkdir -p %{buildroot}%{gem_libdir json}
mkdir -p %{buildroot}%{gem_extdir_mri json}
mv %{buildroot}%{ruby_libdir}/json* %{buildroot}%{gem_libdir json}
mv %{buildroot}%{ruby_libarchdir}/json/ %{buildroot}%{gem_extdir_mri json}
touch %{buildroot}%{gem_extdir_mri json}/gem.build_complete
mv %{buildroot}%{gem_spec -d json} %{buildroot}%{gem_spec json}
ln -s %{gem_libdir json}/json.rb %{buildroot}%{ruby_libdir}/json.rb
ln -s %{gem_libdir json}/json %{buildroot}%{ruby_libdir}/json
ln -s %{gem_extdir_mri json}/json/ %{buildroot}%{ruby_libarchdir}/json

mkdir -p %{buildroot}%{gem_libdir psych}
mkdir -p %{buildroot}%{gem_extdir_mri psych}
mv %{buildroot}%{ruby_libdir}/psych* %{buildroot}%{gem_libdir psych}
mv %{buildroot}%{ruby_libarchdir}/psych.so %{buildroot}%{gem_extdir_mri psych}
touch %{buildroot}%{gem_extdir_mri psych}/gem.build_complete
mv %{buildroot}%{gem_spec -d psych} %{buildroot}%{gem_spec psych}
ln -s %{gem_libdir psych}/psych %{buildroot}%{ruby_libdir}/psych
ln -s %{gem_libdir psych}/psych.rb %{buildroot}%{ruby_libdir}/psych.rb
ln -s %{gem_extdir_mri psych}/psych.so %{buildroot}%{ruby_libarchdir}/psych.so

# Move the binary extensions into proper place (if no gem has binary extension,
# the extensions directory might be empty).
# TODO: Get information about extension form .gemspec files.
find %{buildroot}%{gem_dir}/extensions/*-%{_target_os}/%{major_minor_version}.*/* -maxdepth 0 \
  -exec mv '{}' %{buildroot}%{_libdir}/gems/%{name}/ \; \
  || echo "No gem binary extensions to move."

# Remove the extension sources and library copies from `lib` dir.
find %{buildroot}%{gem_dir}/gems/*/ext -maxdepth 0 -exec rm -rf '{}' +
find %{buildroot}%{gem_dir}/gems/*/lib -name \*.so -delete

# Move man pages into proper location
mkdir -p %{buildroot}%{_mandir}/man{1,5}
mv %{buildroot}%{gem_instdir irb}/man/irb.1 %{buildroot}%{_mandir}/man1
mv %{buildroot}%{gem_instdir rake}/doc/rake.1 %{buildroot}%{_mandir}/man1
mv %{buildroot}%{gem_instdir rdoc}/man/ri.1 %{buildroot}%{_mandir}/man1
# https://bugs.ruby-lang.org/issues/17778
cp -a %{buildroot}%{gem_libdir bundler}/bundler/man/*.1 %{buildroot}%{_mandir}/man1
cp -a %{buildroot}%{gem_libdir bundler}/bundler/man/*.5 %{buildroot}%{_mandir}/man5

%if %{with systemtap}
# Install a tapset and fix up the path to the library.
mkdir -p %{buildroot}%{_systemtap_tapsetdir}
sed -e "s|@LIBRARY_PATH@|%{tapset_libdir}/libruby.so.%{major_minor_version}|" \
  %{SOURCE2} > %{buildroot}%{_systemtap_tapsetdir}/libruby.so.%{major_minor_version}.stp
# Escape '*/' in comment.
sed -i -r "s|( \*.*\*)\/(.*)|\1\\\/\2|" %{buildroot}%{_systemtap_tapsetdir}/libruby.so.%{major_minor_version}.stp
%endif

# Prepare -doc subpackage file lists.
find doc -maxdepth 1 -type f ! -name '.*' ! -name '*.ja*' > .ruby-doc.en
echo 'doc/images' >> .ruby-doc.en
echo 'doc/syntax' >> .ruby-doc.en

find doc -maxdepth 1 -type f -name '*.ja*' > .ruby-doc.ja
echo 'doc/pty' >> .ruby-doc.ja

sed -i 's/^/%doc /' .ruby-doc.*
sed -i 's/^/%lang(ja) /' .ruby-doc.ja

%check
%if 0%{?with_hardening_test}
# Check Ruby hardening.
%define fortification_x86_64  fortified="10" fortify-able="26"
%define fortification_i686    fortified="10" fortify-able="26"
%define fortification_aarch64 fortified="11" fortify-able="28"
%define fortification_ppc64le fortified="7" fortify-able="24"
%define fortification_s390x   fortified="10" fortify-able="24"
%define fortification_riscv64 fortified="10" fortify-able="26"
# https://unix.stackexchange.com/questions/366/convince-grep-to-output-all-lines-not-just-those-with-matches
checksec --format=xml --file=%{_vpath_builddir}/libruby.so.%{ruby_version} | \
  sed -r "s/<file (.*)\/>/\1/" | \
  sed -nr $'/relro="full" canary="yes" nx="yes" pie="dso" rpath="no" runpath="no" symbols="yes" fortify_source="partial" %{expand:%{fortification_%{_target_cpu}}} filename='\''redhat-linux-build\/libruby.so.%{ruby_version}'\''/h; ${p;x;/./Q0;Q1}'
%endif

# Check RubyGems version.
[ "`make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT='%{_builddir}/%{buildsubdir}/bin/gem -v' | tail -1`" == '%{rubygems_version}' ]

# Check Rubygems bundled dependencies versions.

# Molinillo.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Gem; module Resolver; end; end; \
  require 'rubygems/vendor/molinillo/lib/molinillo/gem_metadata'; \
  puts '%%{rubygems_molinillo_version}: %{rubygems_molinillo_version}'; \
  puts %Q[Gem::Molinillo::VERSION: #{Gem::Molinillo::VERSION}]; \
  exit 1 if Gem::Molinillo::VERSION != '%{rubygems_molinillo_version}'; \
\""

# Net::HTTP.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Gem; module Net; end; end; \
  require 'rbconfig'; \
  require 'rubygems/vendor/net-http/lib/net/http'; \
  puts '%%{rubygems_net_http_version}: %{rubygems_net_http_version}'; \
  puts %Q[Gem::Net::HTTP::VERSION: #{Gem::Net::HTTP::VERSION}]; \
  exit 1 if Gem::Net::HTTP::VERSION != '%{rubygems_net_http_version}'; \
\""

# Net::Protocol.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Gem; module Net; end; end; \
  require 'rubygems/vendor/net-protocol/lib/net/protocol'; \
  puts '%%{rubygems_net_protocol_version}: %{rubygems_net_protocol_version}'; \
  puts %Q[Gem::Net::Protocol::VERSION: #{Gem::Net::Protocol::VERSION}]; \
  exit 1 if Gem::Net::Protocol::VERSION != '%{rubygems_net_protocol_version}'; \
\""

# OptParse.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Gem; end; \
  require 'rubygems/vendor/optparse/lib/optparse'; \
  puts '%%{rubygems_optparse_version}: %{rubygems_optparse_version}'; \
  puts %Q[Gem::OptionParser::Version: #{Gem::OptionParser::Version}]; \
  exit 1 if Gem::OptionParser::Version != '%{rubygems_optparse_version}'; \
\""

# Resolv.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Gem; end; \
  require 'rbconfig'; \
  require 'rubygems/vendor/resolv/lib/resolv'; \
  puts '%%{rubygems_resolv_version}: %{rubygems_resolv_version}'; \
  puts %Q[Gem::Resolv::VERSION: #{Gem::Resolv::VERSION}]; \
  exit 1 if Gem::Resolv::VERSION != '%{rubygems_resolv_version}'; \
\""

# SecureRandom.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Gem; module Random; end; end; \
  require 'rubygems/vendor/securerandom/lib/securerandom'; \
  puts '%%{rubygems_securerandom_version}: %{rubygems_securerandom_version}'; \
  puts %Q[Gem::SecureRandom::VERSION: #{Gem::SecureRandom::VERSION}]; \
  exit 1 if Gem::SecureRandom::VERSION != '%{rubygems_securerandom_version}'; \
\""

# Timeout.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Gem; end; \
  require 'rubygems/vendor/timeout/lib/timeout'; \
  puts '%%{rubygems_timeout_version}: %{rubygems_timeout_version}'; \
  puts %Q[Gem::Timeout::VERSION: #{Gem::Timeout::VERSION}]; \
  exit 1 if Gem::Timeout::VERSION != '%{rubygems_timeout_version}'; \
\""

# TSort
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Gem; end; \
  require 'rubygems/vendor/tsort/lib/tsort'; \
  puts '%%{rubygems_tsort_version}: %{rubygems_tsort_version}'; \
  puts %Q[Gem::TSort::VERSION: #{Gem::TSort::VERSION}]; \
  exit 1 if Gem::TSort::VERSION != '%{rubygems_tsort_version}'; \
\""

# URI.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Gem; end; \
  require 'rubygems/vendor/uri/lib/uri/version'; \
  puts '%%{rubygems_uri_version}: %{rubygems_uri_version}'; \
  puts %Q[Gem::URI::VERSION: #{Gem::URI::VERSION}]; \
  exit 1 if Gem::URI::VERSION != '%{rubygems_uri_version}'; \
\""

# Check Bundler bundled dependencies versions.

# connection_pool.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Bundler; end; \
  require 'bundler/vendor/connection_pool/lib/connection_pool/version'; \
  puts '%%{bundler_connection_pool_version}; %{bundler_connection_pool_version}'; \
  puts %Q[Bundler::ConnectionPool::VERSION: #{Bundler::ConnectionPool::VERSION}]; \
  exit 1 if Bundler::ConnectionPool::VERSION != '%{bundler_connection_pool_version}'; \
\""

# FileUtils.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Bundler; end; \
  require 'bundler/vendor/fileutils/lib/fileutils'; \
  puts '%%{bundler_fileutils_version}: %{bundler_fileutils_version}'; \
  puts %Q[Bundler::FileUtils::VERSION: #{Bundler::FileUtils::VERSION}]; \
  exit 1 if Bundler::FileUtils::VERSION != '%{bundler_fileutils_version}'; \
\""

# PubGrub
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Bundler; end; \
  require 'bundler/vendor/pub_grub/lib/pub_grub/version'; \
  puts '%%{bundler_pub_grub_version}: %{bundler_pub_grub_version}'; \
  puts %Q[Bundler::PubGrub::VERSION: #{Bundler::PubGrub::VERSION}]; \
  exit 1 if Bundler::PubGrub::VERSION != '%{bundler_pub_grub_version}'; \
\""

# Net::HTTP::Persistent.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Gem; end; \
  module Bundler; end; \
  require 'rbconfig'; \
  require 'bundler/vendor/net-http-persistent/lib/net/http/persistent'; \
  puts '%%{bundler_net_http_persistent_version}: %{bundler_net_http_persistent_version}'; \
  puts %Q[Gem::Net::HTTP::Persistent::VERSION: #{Gem::Net::HTTP::Persistent::VERSION}]; \
  exit 1 if Gem::Net::HTTP::Persistent::VERSION != '%{bundler_net_http_persistent_version}'; \
\""

# SecureRandom.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Bundler; module Random; end; end; \
  require 'bundler/vendor/securerandom/lib/securerandom'; \
  puts '%%{bundler_securerandom_version}: %{bundler_securerandom_version}'; \
  puts %Q[Bundler::SecureRandom::VERSION: #{Bundler::SecureRandom::VERSION}]; \
  exit 1 if Bundler::SecureRandom::VERSION != '%{bundler_securerandom_version}'; \
\""

# Thor.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Bundler; end; \
  require 'bundler/vendor/thor/lib/thor/version'; \
  puts '%%{bundler_thor_version}: %{bundler_thor_version}'; \
  puts %Q[Bundler::Thor::VERSION: #{Bundler::Thor::VERSION}]; \
  exit 1 if Bundler::Thor::VERSION != '%{bundler_thor_version}'; \
\""

# TSort
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Bundler; end; \
  require 'bundler/vendor/tsort/lib/tsort'; \
  puts '%%{bundler_tsort_version}: %{bundler_tsort_version}'; \
  puts %Q[Bundler::TSort::VERSION: #{Bundler::TSort::VERSION}]; \
  exit 1 if Bundler::TSort::VERSION != '%{bundler_tsort_version}'; \
\""

# URI.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  module Bundler; end; \
  require 'bundler/vendor/uri/lib/uri/version'; \
  puts '%%{bundler_uri_version}: %{bundler_uri_version}'; \
  puts %Q[Bundler::URI::VERSION: #{Bundler::URI::VERSION}]; \
  exit 1 if Bundler::URI::VERSION != '%{bundler_uri_version}'; \
\""

# Check bundled libraries versions.

# Nkf.
make -C %{_vpath_builddir} -s runruby TESTRUN_SCRIPT="-e \" \
  require 'rubygems'; \
  require 'nkf'; \
  puts '%%{bundled_nkf_version}: %{bundled_nkf_version}'; \
  puts %Q[NKF::NKF_VERSION: #{NKF::NKF_VERSION}]; \
  exit 1 if NKF::NKF_VERSION != '%{bundled_nkf_version}'; \
\""


# test_debug(TestRubyOptions) fails due to LoadError reported in debug mode,
# when abrt.rb cannot be required (seems to be easier way then customizing
# the test suite).
touch %{_vpath_builddir}/abrt.rb

# Check if abrt hook is required (RubyGems are disabled by default when using
# runruby, so re-enable them).
make -C %{_vpath_builddir} runruby TESTRUN_SCRIPT="--enable-gems %{SOURCE10}"

# Check if systemtap is supported.
%if %{with systemtap}
ln -sfr probes.d %{_vpath_builddir}/
make -C %{_vpath_builddir} runruby TESTRUN_SCRIPT=%{SOURCE11}
%endif

# Test dependency generators for RPM
GENERATOR_SCRIPT="%{SOURCE7}" \
make -C %{_vpath_builddir} runruby TESTRUN_SCRIPT=" \
  -I%{_builddir}/%{buildsubdir}/tool/lib -I%{_sourcedir} --enable-gems \
  %{SOURCE14} --verbose"
GENERATOR_SCRIPT="%{SOURCE8}" \
make -C %{_vpath_builddir} runruby TESTRUN_SCRIPT=" \
  -I%{_builddir}/%{buildsubdir}/tool/lib -I%{_sourcedir} --enable-gems \
  %{SOURCE15} --verbose"
GENERATOR_SCRIPT="%{SOURCE9}" \
make -C %{_vpath_builddir} runruby TESTRUN_SCRIPT=" \
  -I%{_builddir}/%{buildsubdir}/tool/lib -I%{_sourcedir} --enable-gems \
  %{SOURCE16} --verbose"


DISABLE_TESTS=""
MSPECOPTS=""

# Avoid `hostname' dependency.
%{!?with_hostname:MSPECOPTS="-P 'Socket.gethostname returns the host name'"}

# Give an option to increase the timeout in tests.
# https://bugs.ruby-lang.org/issues/16921
%{?test_timeout_scale:RUBY_TEST_TIMEOUT_SCALE="%{test_timeout_scale}"} \
  make -C %{_vpath_builddir} %{?with_parallel_tests:%{?_smp_mflags}} check TESTS="-v --show-skip $DISABLE_TESTS" MSPECOPT="-fs $MSPECOPTS"

# Run Ruby OpenSSL tests in OpenSSL FIPS.
make -C %{_vpath_builddir} runruby TESTRUN_SCRIPT=" \
  -I%{_builddir}/%{buildsubdir}/tool/lib --enable-gems \
  %{SOURCE12} %{_builddir}/%{buildsubdir} --verbose"

%{?with_bundler_tests:make -C %{_vpath_builddir} test-bundler-parallel}

%files
%license BSDL
%license COPYING
%lang(ja) %license COPYING.ja
%license GPL
%license LEGAL
%{_bindir}/%{name}%{?with_rubypick:-mri}
%{_mandir}/man1/ruby*

%files devel
%license BSDL
%license COPYING
%lang(ja) %license COPYING.ja
%license GPL
%license LEGAL

%{_rpmmacrodir}/macros.ruby

%dir %{_includedir}
%{_includedir}/ruby/
%{_libdir}/libruby.so
%{_libdir}/pkgconfig/%{name}.pc

%files libs
%license COPYING
%lang(ja) %license COPYING.ja
%license GPL
%license LEGAL
%doc README.md
%doc NEWS.md
# Exclude /usr/local directory since it is supposed to be managed by
# local system administrator.
%exclude %{ruby_sitelibdir}
%exclude %{ruby_sitearchdir}
%dir %{ruby_vendorlibdir}
%dir %{ruby_vendorarchdir}

# List all these files explicitly to prevent surprises
# Platform independent libraries.
%dir %{ruby_libdir}
%exclude %{ruby_libdir}/json*
%exclude %{ruby_libdir}/psych*
%{ruby_libdir}/bundled_gems.rb
%{ruby_libdir}/cgi*
%{ruby_libdir}/coverage.rb
%{ruby_libdir}/date.rb
%{ruby_libdir}/delegate*
%{ruby_libdir}/digest*
%{ruby_libdir}/English.rb
%{ruby_libdir}/erb*
%{ruby_libdir}/error_highlight*
%{ruby_libdir}/expect.rb
%{ruby_libdir}/fileutils.rb
%{ruby_libdir}/find.rb
%{ruby_libdir}/forwardable*
%{ruby_libdir}/ipaddr.rb
%{ruby_libdir}/mkmf.rb
%{ruby_libdir}/monitor.rb
%{ruby_libdir}/net
%{ruby_libdir}/objspace*
%{ruby_libdir}/open-uri.rb
%{ruby_libdir}/open3*
%{ruby_libdir}/optionparser.rb
%{ruby_libdir}/optparse*
%{ruby_libdir}/pathname.rb
%{ruby_libdir}/pp.rb
%{ruby_libdir}/prettyprint.rb
%{ruby_libdir}/random
%{ruby_libdir}/resolv.rb
%{ruby_libdir}/ripper*
%{ruby_libdir}/securerandom.rb
%{ruby_libdir}/set/subclass_compatible.rb
%{ruby_libdir}/shellwords.rb
%{ruby_libdir}/singleton*
%{ruby_libdir}/socket.rb
%{ruby_libdir}/strscan
%{ruby_libdir}/syntax_suggest*
%{ruby_libdir}/tempfile.rb
%{ruby_libdir}/timeout*
%{ruby_libdir}/time.rb
%{ruby_libdir}/tmpdir.rb
%{ruby_libdir}/tsort.rb
%{ruby_libdir}/unicode_normalize
%{ruby_libdir}/un.rb
%{ruby_libdir}/uri*
%{ruby_libdir}/weakref*
%{ruby_libdir}/yaml*
%{ruby_libdir}/prism*

# Platform specific libraries.
%{_libdir}/libruby.so.{%{major_minor_version},%{ruby_version}}
%dir %{ruby_libarchdir}
%dir %{ruby_libarchdir}/cgi
%{ruby_libarchdir}/cgi/escape.so
%{ruby_libarchdir}/continuation.so
%{ruby_libarchdir}/coverage.so
%{ruby_libarchdir}/date_core.so
%dir %{ruby_libarchdir}/digest
%{ruby_libarchdir}/digest.so
%{ruby_libarchdir}/digest/bubblebabble.so
%{ruby_libarchdir}/digest/md5.so
%{ruby_libarchdir}/digest/rmd160.so
%{ruby_libarchdir}/digest/sha1.so
%{ruby_libarchdir}/digest/sha2.so
%dir %{ruby_libarchdir}/enc
%{ruby_libarchdir}/enc/big5.so
%{ruby_libarchdir}/enc/cesu_8.so
%{ruby_libarchdir}/enc/cp949.so
%{ruby_libarchdir}/enc/emacs_mule.so
%{ruby_libarchdir}/enc/encdb.so
%{ruby_libarchdir}/enc/euc_jp.so
%{ruby_libarchdir}/enc/euc_kr.so
%{ruby_libarchdir}/enc/euc_tw.so
%{ruby_libarchdir}/enc/gb18030.so
%{ruby_libarchdir}/enc/gb2312.so
%{ruby_libarchdir}/enc/gbk.so
%{ruby_libarchdir}/enc/iso_8859_1.so
%{ruby_libarchdir}/enc/iso_8859_10.so
%{ruby_libarchdir}/enc/iso_8859_11.so
%{ruby_libarchdir}/enc/iso_8859_13.so
%{ruby_libarchdir}/enc/iso_8859_14.so
%{ruby_libarchdir}/enc/iso_8859_15.so
%{ruby_libarchdir}/enc/iso_8859_16.so
%{ruby_libarchdir}/enc/iso_8859_2.so
%{ruby_libarchdir}/enc/iso_8859_3.so
%{ruby_libarchdir}/enc/iso_8859_4.so
%{ruby_libarchdir}/enc/iso_8859_5.so
%{ruby_libarchdir}/enc/iso_8859_6.so
%{ruby_libarchdir}/enc/iso_8859_7.so
%{ruby_libarchdir}/enc/iso_8859_8.so
%{ruby_libarchdir}/enc/iso_8859_9.so
%{ruby_libarchdir}/enc/koi8_r.so
%{ruby_libarchdir}/enc/koi8_u.so
%{ruby_libarchdir}/enc/shift_jis.so
%dir %{ruby_libarchdir}/enc/trans
%{ruby_libarchdir}/enc/trans/big5.so
%{ruby_libarchdir}/enc/trans/cesu_8.so
%{ruby_libarchdir}/enc/trans/chinese.so
%{ruby_libarchdir}/enc/trans/ebcdic.so
%{ruby_libarchdir}/enc/trans/emoji.so
%{ruby_libarchdir}/enc/trans/emoji_iso2022_kddi.so
%{ruby_libarchdir}/enc/trans/emoji_sjis_docomo.so
%{ruby_libarchdir}/enc/trans/emoji_sjis_kddi.so
%{ruby_libarchdir}/enc/trans/emoji_sjis_softbank.so
%{ruby_libarchdir}/enc/trans/escape.so
%{ruby_libarchdir}/enc/trans/gb18030.so
%{ruby_libarchdir}/enc/trans/gbk.so
%{ruby_libarchdir}/enc/trans/iso2022.so
%{ruby_libarchdir}/enc/trans/japanese.so
%{ruby_libarchdir}/enc/trans/japanese_euc.so
%{ruby_libarchdir}/enc/trans/japanese_sjis.so
%{ruby_libarchdir}/enc/trans/korean.so
%{ruby_libarchdir}/enc/trans/single_byte.so
%{ruby_libarchdir}/enc/trans/transdb.so
%{ruby_libarchdir}/enc/trans/utf8_mac.so
%{ruby_libarchdir}/enc/trans/utf_16_32.so
%{ruby_libarchdir}/enc/utf_16be.so
%{ruby_libarchdir}/enc/utf_16le.so
%{ruby_libarchdir}/enc/utf_32be.so
%{ruby_libarchdir}/enc/utf_32le.so
%{ruby_libarchdir}/enc/windows_1250.so
%{ruby_libarchdir}/enc/windows_1251.so
%{ruby_libarchdir}/enc/windows_1252.so
%{ruby_libarchdir}/enc/windows_1253.so
%{ruby_libarchdir}/enc/windows_1254.so
%{ruby_libarchdir}/enc/windows_1257.so
%{ruby_libarchdir}/enc/windows_31j.so
%{ruby_libarchdir}/erb/escape.so
%{ruby_libarchdir}/etc.so
%{ruby_libarchdir}/fcntl.so
%dir %{ruby_libarchdir}/io
%{ruby_libarchdir}/io/nonblock.so
%{ruby_libarchdir}/io/wait.so
%{ruby_libarchdir}/monitor.so
%{ruby_libarchdir}/objspace.so
%{ruby_libarchdir}/pty.so
%dir %{ruby_libarchdir}/rbconfig
%{ruby_libarchdir}/rbconfig.rb
%{ruby_libarchdir}/rbconfig/sizeof.so
%{ruby_libarchdir}/ripper.so
%{ruby_libarchdir}/socket.so
%{ruby_libarchdir}/stringio.so
%{ruby_libarchdir}/strscan.so
%{ruby_libarchdir}/zlib.so

# Default gems
%{ruby_libdir}/did_you_mean*
%{ruby_libdir}/openssl*
%{ruby_libarchdir}/openssl.so

%{?with_systemtap:%{_systemtap_datadir}}

%files -n rubygems
%{_bindir}/gem
%dir %{rubygems_dir}
%{rubygems_dir}/rubygems
%{rubygems_dir}/rubygems.rb

# Explicitly include only RubyGems directory strucure to avoid accidentally
# packaged content.
%dir %{gem_dir}
%dir %{gem_dir}/build_info
%dir %{gem_dir}/cache
%dir %{gem_dir}/doc
%dir %{gem_dir}/extensions
%dir %{gem_dir}/gems
%dir %{gem_dir}/plugins
%dir %{gem_dir}/specifications
%dir %{gem_dir}/specifications/default
%dir %{_exec_prefix}/lib*/gems
%dir %{_exec_prefix}/lib*/gems/ruby

%exclude %{gem_dir}/cache/*

%files -n rubygems-devel
%{_rpmmacrodir}/macros.rubygems
%{_fileattrsdir}/rubygems.attr
%{_rpmconfigdir}/rubygems.req
%{_rpmconfigdir}/rubygems.prov
%{_rpmconfigdir}/rubygems.con

%files default-gems
%gem_spec -d date
%gem_spec -d delegate
%gem_spec -d did_you_mean
%gem_spec -d digest
%gem_spec -d english
%gem_spec -d erb
%gem_instdir erb
%{_bindir}/erb
%{_mandir}/man1/erb*
%gem_spec -d error_highlight
%gem_spec -d etc
%gem_spec -d fcntl
%gem_spec -d fileutils
%gem_spec -d find
%gem_spec -d forwardable
%gem_spec -d io-nonblock
%gem_spec -d io-wait
%gem_spec -d ipaddr
%gem_spec -d net-http
%gem_spec -d net-protocol
%gem_spec -d open3
%gem_spec -d open-uri
%gem_spec -d optparse
%gem_spec -d openssl
%gem_spec -d pp
%gem_spec -d prettyprint
%gem_spec -d resolv
%gem_spec -d ruby2_keywords
%gem_spec -d securerandom
%gem_spec -d shellwords
%gem_spec -d singleton
%gem_spec -d stringio
%gem_spec -d strscan
%gem_spec -d syntax_suggest
%{_bindir}/syntax_suggest
%gem_instdir syntax_suggest
%gem_spec -d tempfile
%gem_spec -d time
%gem_spec -d timeout
%gem_spec -d tmpdir
%gem_spec -d tsort
%gem_spec -d un
%gem_spec -d uri
%gem_spec -d weakref
#%%gem_spec -d win32ole
#%%gem_spec -d win32-registry
%gem_spec -d yaml
%gem_spec -d prism
%gem_spec -d zlib

%files -n rubygem-irb
%{_bindir}/irb
%dir %{gem_instdir irb}
%{gem_libdir irb}
%{gem_spec irb}
%{gem_instdir irb}/exe

%{gem_instdir irb}/Gemfile
%license %{gem_instdir irb}/LICENSE.txt
%doc %{gem_instdir irb}/doc
%doc %{gem_instdir irb}/README.md
%doc %{gem_instdir irb}/CONTRIBUTING.md
%doc %{gem_instdir irb}/EXTEND_IRB.md
%{_mandir}/man1/irb.1*

%files -n rubygem-rdoc
%{_bindir}/rdoc
%{_bindir}/ri
%{gem_instdir rdoc}
%{gem_spec rdoc}
%{gem_plugin rdoc}
%{_mandir}/man1/ri*

%files doc -f .ruby-doc.en -f .ruby-doc.ja
%doc README.md
%doc ChangeLog
%{?with_systemtap:%doc ruby-exercise.stp}
%{_datadir}/ri

%files -n rubygem-bigdecimal
%{gem_extdir_mri bigdecimal}
%{gem_instdir bigdecimal}
%{gem_spec bigdecimal}

%files -n rubygem-io-console
%{ruby_libdir}/io
%{ruby_libarchdir}/io/console.so
%{gem_extdir_mri io-console}
%{gem_instdir io-console}
%{gem_spec io-console}

%files -n rubygem-json
%{ruby_libdir}/json*
%{ruby_libarchdir}/json*
%{gem_extdir_mri json}
%{gem_instdir json}
%{gem_spec json}

%files -n rubygem-psych
%{ruby_libdir}/psych
%{ruby_libdir}/psych.rb
%{ruby_libarchdir}/psych.so
%{gem_extdir_mri psych}
%dir %{gem_instdir psych}
%{gem_libdir psych}
%{gem_spec psych}

%files -n rubygem-bundler
%{_bindir}/bundle
%{_bindir}/bundler
%{gem_instdir bundler}
%{gem_spec bundler}
%{_mandir}/man1/bundle*.1*
%{_mandir}/man5/gemfile.5*

%files bundled-gems
# abbrev
%dir %{gem_instdir abbrev}
%license %{gem_instdir abbrev}/LICENSE.txt
%{gem_instdir abbrev}/bin
%{gem_libdir abbrev}
%{gem_spec abbrev}
%{gem_instdir abbrev}/Gemfile
%doc %{gem_instdir abbrev}/README.md
%{gem_instdir abbrev}/Rakefile

# base64
%dir %{gem_instdir base64}
%license %{gem_instdir base64}/BSDL
%license %{gem_instdir base64}/COPYING
%license %{gem_instdir base64}/LEGAL
%{gem_instdir base64}/sig
%{gem_libdir base64}
%{gem_spec base64}
%doc %{gem_instdir base64}/README.md

# benchmark
%dir %{gem_instdir benchmark}
%license %{gem_instdir benchmark}/BSDL
%license %{gem_instdir benchmark}/COPYING
%doc %{gem_instdir benchmark}/README.md
%{gem_instdir benchmark}/Gemfile
%{gem_instdir benchmark}/Rakefile
%{gem_instdir benchmark}/bin
%{gem_libdir benchmark}
%{gem_spec benchmark}

# csv
%dir %{gem_instdir csv}
%license %{gem_instdir csv}/LICENSE.txt
%doc %{gem_instdir csv}/NEWS.md
%{gem_libdir csv}
%{gem_spec csv}
%doc %{gem_instdir csv}/README.md
%doc %{gem_instdir csv}/doc

# drb
%dir %{gem_instdir drb}
%license %{gem_instdir drb}/LICENSE.txt
%{gem_libdir drb}
%{gem_instdir drb}/drb.gemspec
%{gem_spec drb}

# getoptlong
%dir %{gem_instdir getoptlong}
%license %{gem_instdir getoptlong}/LICENSE.txt
%{gem_instdir getoptlong}/bin
%{gem_libdir getoptlong}
%{gem_instdir getoptlong}/sample
%{gem_spec getoptlong}
%{gem_instdir getoptlong}/Gemfile
%doc %{gem_instdir getoptlong}/README.md
%{gem_instdir getoptlong}/Rakefile

# fiddle
%dir %{gem_instdir fiddle}
%license %{gem_instdir fiddle}/LICENSE.txt
%doc %{gem_instdir fiddle}/README.md
%{gem_instdir fiddle}/Rakefile
%{gem_libdir fiddle}
%dir %{gem_extdir_mri fiddle}
%{gem_extdir_mri fiddle}/fiddle.so
%{gem_extdir_mri fiddle}/gem.build_complete
%{gem_instdir fiddle}/fiddle.gemspec
%{gem_spec fiddle}

# logger
%dir %{gem_instdir logger}
%license %{gem_instdir logger}/BSDL
%license %{gem_instdir logger}/COPYING
%doc %{gem_instdir logger}/README.md
%{gem_libdir logger}
%{gem_spec logger}

# matrix
%dir %{gem_instdir matrix}
%license %{gem_instdir matrix}/BSDL
%license %{gem_instdir matrix}/COPYING
%{gem_libdir matrix}
%{gem_instdir matrix}/matrix.gemspec
%{gem_spec matrix}

# mutex_m
%dir %{gem_instdir mutex_m}
%license %{gem_instdir mutex_m}/BSDL
%license %{gem_instdir mutex_m}/COPYING
%{gem_libdir mutex_m}
%{gem_instdir mutex_m}/sig
%{gem_spec mutex_m}
%doc %{gem_instdir mutex_m}/README.md

# net-ftp
%dir %{gem_instdir net-ftp}
%license %{gem_instdir net-ftp}/BSDL
%license %{gem_instdir net-ftp}/COPYING
%{gem_instdir net-ftp}/Gemfile
%license %{gem_instdir net-ftp}/LICENSE.txt
%doc %{gem_instdir net-ftp}/README.md
%{gem_instdir net-ftp}/Rakefile
%{gem_libdir net-ftp}
%{gem_spec net-ftp}

# net-imap
%dir %{gem_instdir net-imap}
%license %{gem_instdir net-imap}/BSDL
%license %{gem_instdir net-imap}/COPYING
%{gem_instdir net-imap}/Gemfile
%license %{gem_instdir net-imap}/LICENSE.txt
%doc %{gem_instdir net-imap}/README.md
%{gem_instdir net-imap}/Rakefile
%{gem_instdir net-imap}/docs
%{gem_libdir net-imap}
%{gem_instdir net-imap}/rakelib
%{gem_instdir net-imap}/sample
%{gem_spec net-imap}

# net-pop
%dir %{gem_instdir net-pop}
%{gem_instdir net-pop}/Gemfile
%license %{gem_instdir net-pop}/LICENSE.txt
%doc %{gem_instdir net-pop}/README.md
%{gem_instdir net-pop}/Rakefile
%{gem_libdir net-pop}
%{gem_spec net-pop}

# net-smtp
%dir %{gem_instdir net-smtp}
%doc %{gem_instdir net-smtp}/NEWS.md
%doc %{gem_instdir net-smtp}/README.md
%license %{gem_instdir net-smtp}/LICENSE.txt
%{gem_libdir net-smtp}
%{gem_spec net-smtp}

# nkf
%dir %{gem_instdir nkf}
%{gem_extdir_mri nkf}
%license %{gem_instdir nkf}/LICENSE.txt
%{gem_instdir nkf}/bin
%{gem_libdir nkf}
%{gem_spec nkf}
%{gem_instdir nkf}/Gemfile
%doc %{gem_instdir nkf}/README.md
%{gem_instdir nkf}/Rakefile

# observer
%dir %{gem_instdir observer}
%license %{gem_instdir observer}/LICENSE.txt
%{gem_instdir observer}/bin
%{gem_libdir observer}
%exclude %{gem_cache observer}
%{gem_spec observer}
%{gem_instdir observer}/Gemfile
%doc %{gem_instdir observer}/README.md
%{gem_instdir observer}/Rakefile

# ostruct
%dir %{gem_instdir ostruct}
%license %{gem_instdir ostruct}/BSDL
%license %{gem_instdir ostruct}/COPYING
%doc %{gem_instdir ostruct}/README.md
%{gem_instdir ostruct}/Gemfile
%{gem_instdir ostruct}/Rakefile
%{gem_instdir ostruct}/bin
%{gem_libdir ostruct}
%{gem_instdir ostruct}/ostruct.gemspec
%{gem_spec ostruct}

# prime
%dir %{gem_instdir prime}
%license %{gem_instdir prime}/BSDL
%license %{gem_instdir prime}/COPYING
%doc %{gem_instdir prime}/README.md
%{gem_instdir prime}/Rakefile
%{gem_libdir prime}
%{gem_instdir prime}/sig
%{gem_instdir prime}/prime.gemspec
%{gem_spec prime}

# pstore
%dir %{gem_instdir pstore}
%license %{gem_instdir pstore}/BSDL
%license %{gem_instdir pstore}/COPYING
%doc %{gem_instdir pstore}/README.md
%{gem_instdir pstore}/Gemfile
%{gem_instdir pstore}/Rakefile
%{gem_instdir pstore}/bin
%{gem_libdir pstore}
%{gem_spec pstore}

# rdbg
%{_bindir}/rdbg
%dir %{gem_extdir_mri debug}
%{gem_extdir_mri debug}/gem.build_complete
%dir %{gem_extdir_mri debug}/debug
%{gem_extdir_mri debug}/debug/debug.so
%dir %{gem_instdir debug}
%exclude %{gem_instdir debug}/.*
%doc %{gem_instdir debug}/CONTRIBUTING.md
%{gem_instdir debug}/Gemfile
%license %{gem_instdir debug}/LICENSE.txt
%doc %{gem_instdir debug}/README.md
%{gem_instdir debug}/Rakefile
%doc %{gem_instdir debug}/TODO.md
%{gem_instdir debug}/exe
%{gem_libdir debug}
%{gem_instdir debug}/misc
%{gem_spec debug}

# readline
%dir %{gem_instdir readline}
%license %{gem_instdir readline}/BSDL
%license %{gem_instdir readline}/COPYING
%doc %{gem_instdir readline}/README.md
%{gem_libdir readline}
%{gem_spec readline}

# reline
%dir %{gem_instdir reline}
%license %{gem_instdir reline}/BSDL
%license %{gem_instdir reline}/COPYING
%license %{gem_instdir reline}/license_of_rb-readline
%doc %{gem_instdir reline}/README.md
%{gem_libdir reline}
%{gem_spec reline}

# repl_type_completor
%dir %{gem_instdir repl_type_completor}
%license %{gem_instdir repl_type_completor}/LICENSE.txt
%{gem_libdir repl_type_completor}
%{gem_instdir repl_type_completor}/sig
%exclude %{gem_cache repl_type_completor}
%{gem_spec repl_type_completor}
%{gem_instdir repl_type_completor}/Gemfile
%doc %{gem_instdir repl_type_completor}/README.md
%{gem_instdir repl_type_completor}/Rakefile

# rinda
%dir %{gem_instdir rinda}
%license %{gem_instdir rinda}/LICENSE.txt
%{gem_instdir rinda}/bin
%{gem_libdir rinda}
%{gem_spec rinda}
%{gem_instdir rinda}/Gemfile
%doc %{gem_instdir rinda}/README.md
%{gem_instdir rinda}/Rakefile

# resolv-replace
%dir %{gem_instdir resolv-replace}
%license %{gem_instdir resolv-replace}/LICENSE.txt
%{gem_instdir resolv-replace}/bin
%{gem_libdir resolv-replace}
%{gem_spec resolv-replace}
%{gem_instdir resolv-replace}/Gemfile
%doc %{gem_instdir resolv-replace}/README.md
%{gem_instdir resolv-replace}/Rakefile

# syslog
%dir %{gem_instdir syslog}
%{gem_extdir_mri syslog}
%license %{gem_instdir syslog}/BSDL
%license %{gem_instdir syslog}/COPYING
%{gem_instdir syslog}/bin
%{gem_libdir syslog}
%exclude %{gem_cache syslog}
%{gem_spec syslog}
%{gem_instdir syslog}/Gemfile
%doc %{gem_instdir syslog}/README.md
%{gem_instdir syslog}/Rakefile

%files -n rubygem-minitest
%{_bindir}/minitest
%dir %{gem_instdir minitest}
%exclude %{gem_instdir minitest}/.*
%{gem_instdir minitest}/Manifest.txt
%{gem_instdir minitest}/design_rationale.rb
%{gem_instdir minitest}/bin
%{gem_libdir minitest}
%{gem_spec minitest}
%doc %{gem_instdir minitest}/History.rdoc
%doc %{gem_instdir minitest}/README.rdoc
%{gem_instdir minitest}/Rakefile
%{gem_instdir minitest}/test

%files -n rubygem-power_assert
%dir %{gem_instdir power_assert}
%exclude %{gem_instdir power_assert}/.*
%license %{gem_instdir power_assert}/BSDL
%license %{gem_instdir power_assert}/COPYING
%license %{gem_instdir power_assert}/LEGAL
%{gem_libdir power_assert}
%{gem_spec power_assert}
%{gem_instdir power_assert}/Gemfile
%doc %{gem_instdir power_assert}/README.md
%{gem_instdir power_assert}/Rakefile

%files -n rubygem-rake
%{_bindir}/rake
%{gem_instdir rake}
%{gem_spec rake}
%{_mandir}/man1/rake.1*

%files -n rubygem-rbs
%{_bindir}/rbs
%dir %{gem_extdir_mri rbs}
%{gem_extdir_mri rbs}/gem.build_complete
%{gem_extdir_mri rbs}/rbs_extension.so
%dir %{gem_instdir rbs}
%license %{gem_instdir rbs}/BSDL
%doc %{gem_instdir rbs}/CHANGELOG.md
%license %{gem_instdir rbs}/COPYING
%doc %{gem_instdir rbs}/README.md
%{gem_instdir rbs}/Rakefile
%{gem_instdir rbs}/Steepfile
%{gem_instdir rbs}/config.yml
%{gem_instdir rbs}/core
%doc %{gem_instdir rbs}/docs
%{gem_instdir rbs}/exe
%{gem_instdir rbs}/goodcheck.yml
%{gem_instdir rbs}/include
%{gem_libdir rbs}
%{gem_instdir rbs}/schema
%{gem_instdir rbs}/sig
%{gem_instdir rbs}/src
%{gem_instdir rbs}/stdlib
%{gem_spec rbs}

%files -n rubygem-test-unit
%{_bindir}/test-unit
%dir %{gem_instdir test-unit}
%license %{gem_instdir test-unit}/BSDL
%license %{gem_instdir test-unit}/COPYING
%license %{gem_instdir test-unit}/PSFL
%{gem_libdir test-unit}
%{gem_instdir test-unit}/sample
%{gem_instdir test-unit}/bin
%{gem_spec test-unit}
%doc %{gem_instdir test-unit}/README.md
%{gem_instdir test-unit}/Rakefile
%doc %{gem_instdir test-unit}/doc

%files -n rubygem-racc
%dir %{gem_instdir racc}
%{_bindir}/racc
%{gem_extdir_mri racc}
%license %{gem_instdir racc}/BSDL
%license %{gem_instdir racc}/COPYING
%doc %{gem_instdir racc}/ChangeLog
%lang(ja) %doc %{gem_instdir racc}/README.ja.rdoc
%doc %{gem_instdir racc}/README.rdoc
%doc %{gem_instdir racc}/TODO
%{gem_instdir racc}/bin
%doc %{gem_instdir racc}/doc
%{gem_libdir racc}
%{gem_spec racc}

%files -n rubygem-rexml
%dir %{gem_instdir rexml}
%license %{gem_instdir rexml}/LICENSE.txt
%doc %{gem_instdir rexml}/NEWS.md
%doc %{gem_instdir rexml}/doc
%{gem_libdir rexml}
%{gem_spec rexml}
%doc %{gem_instdir rexml}/README.md

%files -n rubygem-rss
%dir %{gem_instdir rss}
%exclude %{gem_instdir rss}/.*
%license %{gem_instdir rss}/LICENSE.txt
%doc %{gem_instdir rss}/NEWS.md
%{gem_libdir rss}
%{gem_spec rss}
%doc %{gem_instdir rss}/README.md

%files -n rubygem-typeprof
%dir %{gem_instdir typeprof}
%{_bindir}/typeprof
%exclude %{gem_instdir typeprof}/.*
%license %{gem_instdir typeprof}/LICENSE
%{gem_instdir typeprof}/bin
%{gem_instdir typeprof}/typeprof.conf.jsonc
%doc %{gem_instdir typeprof}/doc
%{gem_libdir typeprof}
%{gem_spec typeprof}
%doc %{gem_instdir typeprof}/README.md


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.1-33
- Prepare for Oreon 11 (RP1)
