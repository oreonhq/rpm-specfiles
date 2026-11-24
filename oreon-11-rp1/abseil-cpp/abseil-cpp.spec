# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f7e05179df39c45434cad433f5783840bb3788ef322976f9138bc6b72b3a107d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond ctest 1
%bcond mingw %{defined fedora}

%global lib_version 2608.0.0

Name:           abseil-cpp
Version:        20260817.0
Release:        %{autorelease}
Summary:        C++ Common Libraries

License:        Apache-2.0 AND LicenseRef-Fedora-Public-Domain
URL:            https://abseil.io
Source0:        https://github.com/abseil/abseil-cpp/archive/%{version}/abseil-cpp-%{version}.tar.gz

Patch:          abseil-cpp-20260817.0-cctz-mingw.patch

BuildSystem:    cmake

BuildOption(conf): -DABSL_ENABLE_INSTALL:BOOL=ON
BuildOption(conf): -DABSL_FIND_GOOGLETEST:BOOL=ON
BuildOption(conf): -DABSL_USE_EXTERNAL_GOOGLETEST:BOOL=ON
BuildOption(conf): -DCMAKE_BUILD_TYPE:STRING=None
BuildOption(conf): -DCMAKE_CXX_STANDARD:STRING=17
%if %{defined ctest}
BuildOption(conf): -DABSL_BUILD_TESTING:BOOL=ON
%else
BuildOption(conf): -DABSL_BUILD_TESTING:BOOL=OFF
%endif
BuildOption(conf): -DABSL_BUILD_TEST_HELPERS:BOOL=ON
BuildOption(check): --exclude-regex "${skips}"

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  ninja-build

BuildRequires:  gmock-devel
BuildRequires:  gtest-devel

%if %{with mingw}
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
%endif

Provides:       bundled(cctz)

%ifarch s390x
%global _lto_cflags %{nil}
%endif

%description
Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from
Google's own C++ code base, has been extensively tested and used in
production, and is the same code we depend on in our daily coding lives.

In some cases, Abseil provides pieces missing from the C++ standard; in
others, Abseil provides alternatives to the standard for special needs we've
found through usage in the Google code base. We denote those cases clearly
within the library code we provide you.

Abseil is not meant to be a competitor to the standard library; we've just
found that many of these utilities serve a purpose within our code base,
and we now want to provide those resources to the C++ community as a whole.

%package testing
Summary:        Libraries needed for running tests on the installed abseil-cpp
Requires:       abseil-cpp%{?_isa} = %{version}-%{release}

Provides:       bundled(cctz)

%description testing
%{summary}.

%package devel
Summary:        Development files for abseil-cpp
Requires:       abseil-cpp%{?_isa} = %{version}-%{release}
Requires:       abseil-cpp-testing%{?_isa} = %{version}-%{release}

Provides:       bundled(cctz)

%description devel
Development headers for abseil-cpp

%if %{with mingw}
%package -n mingw32-abseil-cpp
Summary:        MinGW Windows abseil-cpp library
BuildArch:      noarch

%description -n mingw32-abseil-cpp
MinGW Windows abseil-cpp library.

%package -n mingw64-abseil-cpp
Summary:        MinGW Windows abseil-cpp library
BuildArch:      noarch

%description -n mingw64-abseil-cpp
MinGW Windows abseil-cpp library.

%{?mingw_debug_package}
%endif

%prep
%oreon_sha256
%autosetup -p1

%if %{with mingw}
%build -a
%mingw_cmake -GNinja -DABSL_BUILD_TESTING:BOOL=OFF
%mingw_ninja --verbose
%endif

%if %{with mingw}
%install -a
%mingw_ninja_install
%mingw_debug_install_post
%endif

%check -p
skips='^($.'
%ifarch ppc64le %{ix86}
skips="${skips}|absl_failure_signal_handler_test"
skips="${skips}|absl_stacktrace_test"
%endif
%ifarch %{ix86}
skips="${skips}|absl_kernel_timeout_internal_test"
skips="${skips}|absl_raw_hash_set_test"
%endif
skips="${skips})$"

%files
%license LICENSE
%doc FAQ.md README.md UPGRADES.md
%{_libdir}/libabsl_base.so.%{lib_version}
%{_libdir}/libabsl_base_cpu_detect.so.%{lib_version}
%{_libdir}/libabsl_city.so.%{lib_version}
%{_libdir}/libabsl_civil_time.so.%{lib_version}
%{_libdir}/libabsl_clock_interface.so.%{lib_version}
%{_libdir}/libabsl_cord.so.%{lib_version}
%{_libdir}/libabsl_cord_internal.so.%{lib_version}
%{_libdir}/libabsl_cordz_functions.so.%{lib_version}
%{_libdir}/libabsl_cordz_handle.so.%{lib_version}
%{_libdir}/libabsl_cordz_info.so.%{lib_version}
%{_libdir}/libabsl_cordz_sample_token.so.%{lib_version}
%{_libdir}/libabsl_crc32c.so.%{lib_version}
%{_libdir}/libabsl_crc_cord_state.so.%{lib_version}
%{_libdir}/libabsl_crc_internal.so.%{lib_version}
%{_libdir}/libabsl_debugging_internal.so.%{lib_version}
%{_libdir}/libabsl_decode_rust_punycode.so.%{lib_version}
%{_libdir}/libabsl_demangle_internal.so.%{lib_version}
%{_libdir}/libabsl_demangle_rust.so.%{lib_version}
%{_libdir}/libabsl_die_if_null.so.%{lib_version}
%{_libdir}/libabsl_examine_stack.so.%{lib_version}
%{_libdir}/libabsl_exponential_biased.so.%{lib_version}
%{_libdir}/libabsl_failure_signal_handler.so.%{lib_version}
%{_libdir}/libabsl_flags_commandlineflag.so.%{lib_version}
%{_libdir}/libabsl_flags_commandlineflag_internal.so.%{lib_version}
%{_libdir}/libabsl_flags_config.so.%{lib_version}
%{_libdir}/libabsl_flags_internal.so.%{lib_version}
%{_libdir}/libabsl_flags_marshalling.so.%{lib_version}
%{_libdir}/libabsl_flags_parse.so.%{lib_version}
%{_libdir}/libabsl_flags_private_handle_accessor.so.%{lib_version}
%{_libdir}/libabsl_flags_program_name.so.%{lib_version}
%{_libdir}/libabsl_flags_reflection.so.%{lib_version}
%{_libdir}/libabsl_flags_usage.so.%{lib_version}
%{_libdir}/libabsl_flags_usage_internal.so.%{lib_version}
%{_libdir}/libabsl_generic_printer_internal.so.%{lib_version}
%{_libdir}/libabsl_graphcycles_internal.so.%{lib_version}
%{_libdir}/libabsl_hardening.so.%{lib_version}
%{_libdir}/libabsl_hash.so.%{lib_version}
%{_libdir}/libabsl_hashtable_profiler.so.%{lib_version}
%{_libdir}/libabsl_hashtablez_sampler.so.%{lib_version}
%{_libdir}/libabsl_int128.so.%{lib_version}
%{_libdir}/libabsl_kernel_timeout_internal.so.%{lib_version}
%{_libdir}/libabsl_leak_check.so.%{lib_version}
%{_libdir}/libabsl_log_entry.so.%{lib_version}
%{_libdir}/libabsl_log_flags.so.%{lib_version}
%{_libdir}/libabsl_log_globals.so.%{lib_version}
%{_libdir}/libabsl_log_initialize.so.%{lib_version}
%{_libdir}/libabsl_log_internal_check_op.so.%{lib_version}
%{_libdir}/libabsl_log_internal_conditions.so.%{lib_version}
%{_libdir}/libabsl_log_internal_fnmatch.so.%{lib_version}
%{_libdir}/libabsl_log_internal_format.so.%{lib_version}
%{_libdir}/libabsl_log_internal_globals.so.%{lib_version}
%{_libdir}/libabsl_log_internal_log_sink_set.so.%{lib_version}
%{_libdir}/libabsl_log_internal_message.so.%{lib_version}
%{_libdir}/libabsl_log_internal_nullguard.so.%{lib_version}
%{_libdir}/libabsl_log_internal_proto.so.%{lib_version}
%{_libdir}/libabsl_log_internal_structured_proto.so.%{lib_version}
%{_libdir}/libabsl_log_severity.so.%{lib_version}
%{_libdir}/libabsl_log_sink.so.%{lib_version}
%{_libdir}/libabsl_malloc_internal.so.%{lib_version}
%{_libdir}/libabsl_periodic_sampler.so.%{lib_version}
%{_libdir}/libabsl_poison.so.%{lib_version}
%{_libdir}/libabsl_profile_builder.so.%{lib_version}
%{_libdir}/libabsl_random_distributions.so.%{lib_version}
%{_libdir}/libabsl_random_internal_distribution_test_util.so.%{lib_version}
%{_libdir}/libabsl_random_internal_entropy_pool.so.%{lib_version}
%{_libdir}/libabsl_random_internal_platform.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen_hwaes.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen_hwaes_impl.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen_slow.so.%{lib_version}
%{_libdir}/libabsl_random_internal_seed_material.so.%{lib_version}
%{_libdir}/libabsl_random_seed_gen_exception.so.%{lib_version}
%{_libdir}/libabsl_random_seed_sequences.so.%{lib_version}
%{_libdir}/libabsl_raw_hash_set.so.%{lib_version}
%{_libdir}/libabsl_raw_logging_internal.so.%{lib_version}
%{_libdir}/libabsl_scoped_set_env.so.%{lib_version}
%{_libdir}/libabsl_source_location.so.%{lib_version}
%{_libdir}/libabsl_spinlock_wait.so.%{lib_version}
%{_libdir}/libabsl_stacktrace.so.%{lib_version}
%{_libdir}/libabsl_status.so.%{lib_version}
%{_libdir}/libabsl_status_builder.so.%{lib_version}
%{_libdir}/libabsl_statusor.so.%{lib_version}
%{_libdir}/libabsl_str_format_internal.so.%{lib_version}
%{_libdir}/libabsl_strerror.so.%{lib_version}
%{_libdir}/libabsl_strings.so.%{lib_version}
%{_libdir}/libabsl_strings_internal.so.%{lib_version}
%{_libdir}/libabsl_symbolize.so.%{lib_version}
%{_libdir}/libabsl_synchronization.so.%{lib_version}
%{_libdir}/libabsl_throw_delegate.so.%{lib_version}
%{_libdir}/libabsl_time.so.%{lib_version}
%{_libdir}/libabsl_time_zone.so.%{lib_version}
%{_libdir}/libabsl_tracing_internal.so.%{lib_version}
%{_libdir}/libabsl_utf8_for_code_point.so.%{lib_version}
%{_libdir}/libabsl_vlog_config_internal.so.%{lib_version}

%files testing
%{_libdir}/libabsl_exception_safety_testing.so.%{lib_version}
%{_libdir}/libabsl_atomic_hook_test_helper.so.%{lib_version}
%{_libdir}/libabsl_spinlock_test_common.so.%{lib_version}
%{_libdir}/libabsl_test_instance_tracker.so.%{lib_version}
%{_libdir}/libabsl_hash_generator_testing.so.%{lib_version}
%{_libdir}/libabsl_stack_consumption.so.%{lib_version}
%{_libdir}/libabsl_log_internal_test_actions.so.%{lib_version}
%{_libdir}/libabsl_log_internal_test_helpers.so.%{lib_version}
%{_libdir}/libabsl_log_internal_test_matchers.so.%{lib_version}
%{_libdir}/libabsl_scoped_mock_log.so.%{lib_version}
%{_libdir}/libabsl_status_matchers.so.%{lib_version}
%{_libdir}/libabsl_pow10_helper.so.%{lib_version}
%{_libdir}/libabsl_per_thread_sem_test_common.so.%{lib_version}
%{_libdir}/libabsl_simulated_clock.so.%{lib_version}
%{_libdir}/libabsl_time_internal_test_util.so.%{lib_version}

%files devel
%{_includedir}/absl
%{_libdir}/libabsl_*.so
%{_libdir}/cmake/absl
%{_libdir}/pkgconfig/absl_*.pc

%if %{with mingw}
%files -n mingw32-abseil-cpp
%license LICENSE
%{mingw32_bindir}/libabsl_base.dll
%{mingw32_bindir}/libabsl_base_cpu_detect.dll
%{mingw32_bindir}/libabsl_city.dll
%{mingw32_bindir}/libabsl_civil_time.dll
%{mingw32_bindir}/libabsl_clock_interface.dll
%{mingw32_bindir}/libabsl_cord.dll
%{mingw32_bindir}/libabsl_cord_internal.dll
%{mingw32_bindir}/libabsl_cordz_functions.dll
%{mingw32_bindir}/libabsl_cordz_handle.dll
%{mingw32_bindir}/libabsl_cordz_info.dll
%{mingw32_bindir}/libabsl_cordz_sample_token.dll
%{mingw32_bindir}/libabsl_crc32c.dll
%{mingw32_bindir}/libabsl_crc_cord_state.dll
%{mingw32_bindir}/libabsl_crc_internal.dll
%{mingw32_bindir}/libabsl_debugging_internal.dll
%{mingw32_bindir}/libabsl_decode_rust_punycode.dll
%{mingw32_bindir}/libabsl_demangle_internal.dll
%{mingw32_bindir}/libabsl_demangle_rust.dll
%{mingw32_bindir}/libabsl_die_if_null.dll
%{mingw32_bindir}/libabsl_examine_stack.dll
%{mingw32_bindir}/libabsl_exponential_biased.dll
%{mingw32_bindir}/libabsl_failure_signal_handler.dll
%{mingw32_bindir}/libabsl_flags_commandlineflag.dll
%{mingw32_bindir}/libabsl_flags_commandlineflag_internal.dll
%{mingw32_bindir}/libabsl_flags_config.dll
%{mingw32_bindir}/libabsl_flags_internal.dll
%{mingw32_bindir}/libabsl_flags_marshalling.dll
%{mingw32_bindir}/libabsl_flags_parse.dll
%{mingw32_bindir}/libabsl_flags_private_handle_accessor.dll
%{mingw32_bindir}/libabsl_flags_program_name.dll
%{mingw32_bindir}/libabsl_flags_reflection.dll
%{mingw32_bindir}/libabsl_flags_usage.dll
%{mingw32_bindir}/libabsl_flags_usage_internal.dll
%{mingw32_bindir}/libabsl_generic_printer_internal.dll
%{mingw32_bindir}/libabsl_graphcycles_internal.dll
%{mingw32_bindir}/libabsl_hardening.dll
%{mingw32_bindir}/libabsl_hash.dll
%{mingw32_bindir}/libabsl_hashtable_profiler.dll
%{mingw32_bindir}/libabsl_hashtablez_sampler.dll
%{mingw32_bindir}/libabsl_int128.dll
%{mingw32_bindir}/libabsl_kernel_timeout_internal.dll
%{mingw32_bindir}/libabsl_leak_check.dll
%{mingw32_bindir}/libabsl_log_entry.dll
%{mingw32_bindir}/libabsl_log_flags.dll
%{mingw32_bindir}/libabsl_log_globals.dll
%{mingw32_bindir}/libabsl_log_initialize.dll
%{mingw32_bindir}/libabsl_log_internal_check_op.dll
%{mingw32_bindir}/libabsl_log_internal_conditions.dll
%{mingw32_bindir}/libabsl_log_internal_fnmatch.dll
%{mingw32_bindir}/libabsl_log_internal_format.dll
%{mingw32_bindir}/libabsl_log_internal_globals.dll
%{mingw32_bindir}/libabsl_log_internal_log_sink_set.dll
%{mingw32_bindir}/libabsl_log_internal_message.dll
%{mingw32_bindir}/libabsl_log_internal_nullguard.dll
%{mingw32_bindir}/libabsl_log_internal_proto.dll
%{mingw32_bindir}/libabsl_log_internal_structured_proto.dll
%{mingw32_bindir}/libabsl_log_severity.dll
%{mingw32_bindir}/libabsl_log_sink.dll
%{mingw32_bindir}/libabsl_malloc_internal.dll
%{mingw32_bindir}/libabsl_periodic_sampler.dll
%{mingw32_bindir}/libabsl_poison.dll
%{mingw32_bindir}/libabsl_profile_builder.dll
%{mingw32_bindir}/libabsl_random_distributions.dll
%{mingw32_bindir}/libabsl_random_internal_distribution_test_util.dll
%{mingw32_bindir}/libabsl_random_internal_entropy_pool.dll
%{mingw32_bindir}/libabsl_random_internal_platform.dll
%{mingw32_bindir}/libabsl_random_internal_randen.dll
%{mingw32_bindir}/libabsl_random_internal_randen_hwaes.dll
%{mingw32_bindir}/libabsl_random_internal_randen_hwaes_impl.dll
%{mingw32_bindir}/libabsl_random_internal_randen_slow.dll
%{mingw32_bindir}/libabsl_random_internal_seed_material.dll
%{mingw32_bindir}/libabsl_random_seed_gen_exception.dll
%{mingw32_bindir}/libabsl_random_seed_sequences.dll
%{mingw32_bindir}/libabsl_raw_hash_set.dll
%{mingw32_bindir}/libabsl_raw_logging_internal.dll
%{mingw32_bindir}/libabsl_scoped_set_env.dll
%{mingw32_bindir}/libabsl_source_location.dll
%{mingw32_bindir}/libabsl_spinlock_wait.dll
%{mingw32_bindir}/libabsl_stacktrace.dll
%{mingw32_bindir}/libabsl_status.dll
%{mingw32_bindir}/libabsl_status_builder.dll
%{mingw32_bindir}/libabsl_statusor.dll
%{mingw32_bindir}/libabsl_strerror.dll
%{mingw32_bindir}/libabsl_str_format_internal.dll
%{mingw32_bindir}/libabsl_strings.dll
%{mingw32_bindir}/libabsl_strings_internal.dll
%{mingw32_bindir}/libabsl_symbolize.dll
%{mingw32_bindir}/libabsl_synchronization.dll
%{mingw32_bindir}/libabsl_throw_delegate.dll
%{mingw32_bindir}/libabsl_time.dll
%{mingw32_bindir}/libabsl_time_zone.dll
%{mingw32_bindir}/libabsl_tracing_internal.dll
%{mingw32_bindir}/libabsl_utf8_for_code_point.dll
%{mingw32_bindir}/libabsl_vlog_config_internal.dll
%{mingw32_includedir}/absl/
%{mingw32_libdir}/libabsl_*.dll.a
%{mingw32_libdir}/cmake/absl/
%{mingw32_libdir}/pkgconfig/absl_*.pc

%files -n mingw64-abseil-cpp
%license LICENSE
%{mingw64_bindir}/libabsl_base.dll
%{mingw64_bindir}/libabsl_base_cpu_detect.dll
%{mingw64_bindir}/libabsl_city.dll
%{mingw64_bindir}/libabsl_civil_time.dll
%{mingw64_bindir}/libabsl_clock_interface.dll
%{mingw64_bindir}/libabsl_cord.dll
%{mingw64_bindir}/libabsl_cord_internal.dll
%{mingw64_bindir}/libabsl_cordz_functions.dll
%{mingw64_bindir}/libabsl_cordz_handle.dll
%{mingw64_bindir}/libabsl_cordz_info.dll
%{mingw64_bindir}/libabsl_cordz_sample_token.dll
%{mingw64_bindir}/libabsl_crc32c.dll
%{mingw64_bindir}/libabsl_crc_cord_state.dll
%{mingw64_bindir}/libabsl_crc_internal.dll
%{mingw64_bindir}/libabsl_debugging_internal.dll
%{mingw64_bindir}/libabsl_decode_rust_punycode.dll
%{mingw64_bindir}/libabsl_demangle_internal.dll
%{mingw64_bindir}/libabsl_demangle_rust.dll
%{mingw64_bindir}/libabsl_die_if_null.dll
%{mingw64_bindir}/libabsl_examine_stack.dll
%{mingw64_bindir}/libabsl_exponential_biased.dll
%{mingw64_bindir}/libabsl_failure_signal_handler.dll
%{mingw64_bindir}/libabsl_flags_commandlineflag.dll
%{mingw64_bindir}/libabsl_flags_commandlineflag_internal.dll
%{mingw64_bindir}/libabsl_flags_config.dll
%{mingw64_bindir}/libabsl_flags_internal.dll
%{mingw64_bindir}/libabsl_flags_marshalling.dll
%{mingw64_bindir}/libabsl_flags_parse.dll
%{mingw64_bindir}/libabsl_flags_private_handle_accessor.dll
%{mingw64_bindir}/libabsl_flags_program_name.dll
%{mingw64_bindir}/libabsl_flags_reflection.dll
%{mingw64_bindir}/libabsl_flags_usage.dll
%{mingw64_bindir}/libabsl_flags_usage_internal.dll
%{mingw64_bindir}/libabsl_generic_printer_internal.dll
%{mingw64_bindir}/libabsl_graphcycles_internal.dll
%{mingw64_bindir}/libabsl_hardening.dll
%{mingw64_bindir}/libabsl_hash.dll
%{mingw64_bindir}/libabsl_hashtable_profiler.dll
%{mingw64_bindir}/libabsl_hashtablez_sampler.dll
%{mingw64_bindir}/libabsl_int128.dll
%{mingw64_bindir}/libabsl_kernel_timeout_internal.dll
%{mingw64_bindir}/libabsl_leak_check.dll
%{mingw64_bindir}/libabsl_log_entry.dll
%{mingw64_bindir}/libabsl_log_flags.dll
%{mingw64_bindir}/libabsl_log_globals.dll
%{mingw64_bindir}/libabsl_log_initialize.dll
%{mingw64_bindir}/libabsl_log_internal_check_op.dll
%{mingw64_bindir}/libabsl_log_internal_conditions.dll
%{mingw64_bindir}/libabsl_log_internal_fnmatch.dll
%{mingw64_bindir}/libabsl_log_internal_format.dll
%{mingw64_bindir}/libabsl_log_internal_globals.dll
%{mingw64_bindir}/libabsl_log_internal_log_sink_set.dll
%{mingw64_bindir}/libabsl_log_internal_message.dll
%{mingw64_bindir}/libabsl_log_internal_nullguard.dll
%{mingw64_bindir}/libabsl_log_internal_proto.dll
%{mingw64_bindir}/libabsl_log_internal_structured_proto.dll
%{mingw64_bindir}/libabsl_log_severity.dll
%{mingw64_bindir}/libabsl_log_sink.dll
%{mingw64_bindir}/libabsl_malloc_internal.dll
%{mingw64_bindir}/libabsl_periodic_sampler.dll
%{mingw64_bindir}/libabsl_poison.dll
%{mingw64_bindir}/libabsl_profile_builder.dll
%{mingw64_bindir}/libabsl_random_distributions.dll
%{mingw64_bindir}/libabsl_random_internal_distribution_test_util.dll
%{mingw64_bindir}/libabsl_random_internal_entropy_pool.dll
%{mingw64_bindir}/libabsl_random_internal_platform.dll
%{mingw64_bindir}/libabsl_random_internal_randen.dll
%{mingw64_bindir}/libabsl_random_internal_randen_hwaes.dll
%{mingw64_bindir}/libabsl_random_internal_randen_hwaes_impl.dll
%{mingw64_bindir}/libabsl_random_internal_randen_slow.dll
%{mingw64_bindir}/libabsl_random_internal_seed_material.dll
%{mingw64_bindir}/libabsl_random_seed_gen_exception.dll
%{mingw64_bindir}/libabsl_random_seed_sequences.dll
%{mingw64_bindir}/libabsl_raw_hash_set.dll
%{mingw64_bindir}/libabsl_raw_logging_internal.dll
%{mingw64_bindir}/libabsl_scoped_set_env.dll
%{mingw64_bindir}/libabsl_source_location.dll
%{mingw64_bindir}/libabsl_spinlock_wait.dll
%{mingw64_bindir}/libabsl_stacktrace.dll
%{mingw64_bindir}/libabsl_status.dll
%{mingw64_bindir}/libabsl_status_builder.dll
%{mingw64_bindir}/libabsl_statusor.dll
%{mingw64_bindir}/libabsl_strerror.dll
%{mingw64_bindir}/libabsl_str_format_internal.dll
%{mingw64_bindir}/libabsl_strings.dll
%{mingw64_bindir}/libabsl_strings_internal.dll
%{mingw64_bindir}/libabsl_symbolize.dll
%{mingw64_bindir}/libabsl_synchronization.dll
%{mingw64_bindir}/libabsl_throw_delegate.dll
%{mingw64_bindir}/libabsl_time.dll
%{mingw64_bindir}/libabsl_time_zone.dll
%{mingw64_bindir}/libabsl_tracing_internal.dll
%{mingw64_bindir}/libabsl_utf8_for_code_point.dll
%{mingw64_bindir}/libabsl_vlog_config_internal.dll
%{mingw64_includedir}/absl/
%{mingw64_libdir}/libabsl_*.dll.a
%{mingw64_libdir}/cmake/absl/
%{mingw64_libdir}/pkgconfig/absl_*.pc
%endif

%changelog
%autochangelog
