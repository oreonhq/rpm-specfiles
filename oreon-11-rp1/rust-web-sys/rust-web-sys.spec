%global source0_hash 8622dcb61c0bcc9fffa6938bed81210af2da9a7e4a1a834b2e37a59b6dfb6141
%bcond check 0
%global debug_package %{nil}
%global crate web-sys
Name:           rust-web-sys
Version:        0.3.103
Release:        1%{?dist}
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/web-sys
Source0:        https://static.crates.io/crates/web-sys/web-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+AbortController-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AbortController-devel

This package contains library source intended for building other packages which
use the "AbortController" feature of the "%{crate}" crate.

%package     -n %{name}+AbortSignal-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AbortSignal-devel

This package contains library source intended for building other packages which
use the "AbortSignal" feature of the "%{crate}" crate.

%package     -n %{name}+AbstractRange-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AbstractRange-devel

This package contains library source intended for building other packages which
use the "AbstractRange" feature of the "%{crate}" crate.

%package     -n %{name}+AddEventListenerOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AddEventListenerOptions-devel

This package contains library source intended for building other packages which
use the "AddEventListenerOptions" feature of the "%{crate}" crate.

%package     -n %{name}+AesCbcParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AesCbcParams-devel

This package contains library source intended for building other packages which
use the "AesCbcParams" feature of the "%{crate}" crate.

%package     -n %{name}+AesCtrParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AesCtrParams-devel

This package contains library source intended for building other packages which
use the "AesCtrParams" feature of the "%{crate}" crate.

%package     -n %{name}+AesDerivedKeyParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AesDerivedKeyParams-devel

This package contains library source intended for building other packages which
use the "AesDerivedKeyParams" feature of the "%{crate}" crate.

%package     -n %{name}+AesGcmParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AesGcmParams-devel

This package contains library source intended for building other packages which
use the "AesGcmParams" feature of the "%{crate}" crate.

%package     -n %{name}+AesKeyAlgorithm-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AesKeyAlgorithm-devel

This package contains library source intended for building other packages which
use the "AesKeyAlgorithm" feature of the "%{crate}" crate.

%package     -n %{name}+AesKeyGenParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AesKeyGenParams-devel

This package contains library source intended for building other packages which
use the "AesKeyGenParams" feature of the "%{crate}" crate.

%package     -n %{name}+Algorithm-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Algorithm-devel

This package contains library source intended for building other packages which
use the "Algorithm" feature of the "%{crate}" crate.

%package     -n %{name}+AlignSetting-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AlignSetting-devel

This package contains library source intended for building other packages which
use the "AlignSetting" feature of the "%{crate}" crate.

%package     -n %{name}+AllowedBluetoothDevice-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AllowedBluetoothDevice-devel

This package contains library source intended for building other packages which
use the "AllowedBluetoothDevice" feature of the "%{crate}" crate.

%package     -n %{name}+AllowedUsbDevice-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AllowedUsbDevice-devel

This package contains library source intended for building other packages which
use the "AllowedUsbDevice" feature of the "%{crate}" crate.

%package     -n %{name}+AlphaOption-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AlphaOption-devel

This package contains library source intended for building other packages which
use the "AlphaOption" feature of the "%{crate}" crate.

%package     -n %{name}+AnalyserNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AnalyserNode-devel

This package contains library source intended for building other packages which
use the "AnalyserNode" feature of the "%{crate}" crate.

%package     -n %{name}+AnalyserOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AnalyserOptions-devel

This package contains library source intended for building other packages which
use the "AnalyserOptions" feature of the "%{crate}" crate.

%package     -n %{name}+AngleInstancedArrays-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AngleInstancedArrays-devel

This package contains library source intended for building other packages which
use the "AngleInstancedArrays" feature of the "%{crate}" crate.

%package     -n %{name}+Animation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Animation-devel

This package contains library source intended for building other packages which
use the "Animation" feature of the "%{crate}" crate.

%package     -n %{name}+AnimationEffect-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AnimationEffect-devel

This package contains library source intended for building other packages which
use the "AnimationEffect" feature of the "%{crate}" crate.

%package     -n %{name}+AnimationEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AnimationEvent-devel

This package contains library source intended for building other packages which
use the "AnimationEvent" feature of the "%{crate}" crate.

%package     -n %{name}+AnimationEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AnimationEventInit-devel

This package contains library source intended for building other packages which
use the "AnimationEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+AnimationPlayState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AnimationPlayState-devel

This package contains library source intended for building other packages which
use the "AnimationPlayState" feature of the "%{crate}" crate.

%package     -n %{name}+AnimationPlaybackEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AnimationPlaybackEvent-devel

This package contains library source intended for building other packages which
use the "AnimationPlaybackEvent" feature of the "%{crate}" crate.

%package     -n %{name}+AnimationPlaybackEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AnimationPlaybackEventInit-devel

This package contains library source intended for building other packages which
use the "AnimationPlaybackEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+AnimationPropertyDetails-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AnimationPropertyDetails-devel

This package contains library source intended for building other packages which
use the "AnimationPropertyDetails" feature of the "%{crate}" crate.

%package     -n %{name}+AnimationPropertyValueDetails-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AnimationPropertyValueDetails-devel

This package contains library source intended for building other packages which
use the "AnimationPropertyValueDetails" feature of the "%{crate}" crate.

%package     -n %{name}+AnimationTimeline-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AnimationTimeline-devel

This package contains library source intended for building other packages which
use the "AnimationTimeline" feature of the "%{crate}" crate.

%package     -n %{name}+AssignedNodesOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AssignedNodesOptions-devel

This package contains library source intended for building other packages which
use the "AssignedNodesOptions" feature of the "%{crate}" crate.

%package     -n %{name}+AttestationConveyancePreference-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AttestationConveyancePreference-devel

This package contains library source intended for building other packages which
use the "AttestationConveyancePreference" feature of the "%{crate}" crate.

%package     -n %{name}+Attr-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Attr-devel

This package contains library source intended for building other packages which
use the "Attr" feature of the "%{crate}" crate.

%package     -n %{name}+AttributeNameValue-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AttributeNameValue-devel

This package contains library source intended for building other packages which
use the "AttributeNameValue" feature of the "%{crate}" crate.

%package     -n %{name}+AudioBuffer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioBuffer-devel

This package contains library source intended for building other packages which
use the "AudioBuffer" feature of the "%{crate}" crate.

%package     -n %{name}+AudioBufferOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioBufferOptions-devel

This package contains library source intended for building other packages which
use the "AudioBufferOptions" feature of the "%{crate}" crate.

%package     -n %{name}+AudioBufferSourceNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioBufferSourceNode-devel

This package contains library source intended for building other packages which
use the "AudioBufferSourceNode" feature of the "%{crate}" crate.

%package     -n %{name}+AudioBufferSourceOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioBufferSourceOptions-devel

This package contains library source intended for building other packages which
use the "AudioBufferSourceOptions" feature of the "%{crate}" crate.

%package     -n %{name}+AudioConfiguration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioConfiguration-devel

This package contains library source intended for building other packages which
use the "AudioConfiguration" feature of the "%{crate}" crate.

%package     -n %{name}+AudioContext-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioContext-devel

This package contains library source intended for building other packages which
use the "AudioContext" feature of the "%{crate}" crate.

%package     -n %{name}+AudioContextLatencyCategory-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioContextLatencyCategory-devel

This package contains library source intended for building other packages which
use the "AudioContextLatencyCategory" feature of the "%{crate}" crate.

%package     -n %{name}+AudioContextOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioContextOptions-devel

This package contains library source intended for building other packages which
use the "AudioContextOptions" feature of the "%{crate}" crate.

%package     -n %{name}+AudioContextState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioContextState-devel

This package contains library source intended for building other packages which
use the "AudioContextState" feature of the "%{crate}" crate.

%package     -n %{name}+AudioData-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioData-devel

This package contains library source intended for building other packages which
use the "AudioData" feature of the "%{crate}" crate.

%package     -n %{name}+AudioDataCopyToOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioDataCopyToOptions-devel

This package contains library source intended for building other packages which
use the "AudioDataCopyToOptions" feature of the "%{crate}" crate.

%package     -n %{name}+AudioDataInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioDataInit-devel

This package contains library source intended for building other packages which
use the "AudioDataInit" feature of the "%{crate}" crate.

%package     -n %{name}+AudioDecoder-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioDecoder-devel

This package contains library source intended for building other packages which
use the "AudioDecoder" feature of the "%{crate}" crate.

%package     -n %{name}+AudioDecoderConfig-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioDecoderConfig-devel

This package contains library source intended for building other packages which
use the "AudioDecoderConfig" feature of the "%{crate}" crate.

%package     -n %{name}+AudioDecoderInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioDecoderInit-devel

This package contains library source intended for building other packages which
use the "AudioDecoderInit" feature of the "%{crate}" crate.

%package     -n %{name}+AudioDecoderSupport-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioDecoderSupport-devel

This package contains library source intended for building other packages which
use the "AudioDecoderSupport" feature of the "%{crate}" crate.

%package     -n %{name}+AudioDestinationNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioDestinationNode-devel

This package contains library source intended for building other packages which
use the "AudioDestinationNode" feature of the "%{crate}" crate.

%package     -n %{name}+AudioEncoder-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioEncoder-devel

This package contains library source intended for building other packages which
use the "AudioEncoder" feature of the "%{crate}" crate.

%package     -n %{name}+AudioEncoderConfig-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioEncoderConfig-devel

This package contains library source intended for building other packages which
use the "AudioEncoderConfig" feature of the "%{crate}" crate.

%package     -n %{name}+AudioEncoderInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioEncoderInit-devel

This package contains library source intended for building other packages which
use the "AudioEncoderInit" feature of the "%{crate}" crate.

%package     -n %{name}+AudioEncoderSupport-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioEncoderSupport-devel

This package contains library source intended for building other packages which
use the "AudioEncoderSupport" feature of the "%{crate}" crate.

%package     -n %{name}+AudioListener-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioListener-devel

This package contains library source intended for building other packages which
use the "AudioListener" feature of the "%{crate}" crate.

%package     -n %{name}+AudioNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioNode-devel

This package contains library source intended for building other packages which
use the "AudioNode" feature of the "%{crate}" crate.

%package     -n %{name}+AudioNodeOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioNodeOptions-devel

This package contains library source intended for building other packages which
use the "AudioNodeOptions" feature of the "%{crate}" crate.

%package     -n %{name}+AudioParam-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioParam-devel

This package contains library source intended for building other packages which
use the "AudioParam" feature of the "%{crate}" crate.

%package     -n %{name}+AudioParamMap-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioParamMap-devel

This package contains library source intended for building other packages which
use the "AudioParamMap" feature of the "%{crate}" crate.

%package     -n %{name}+AudioProcessingEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioProcessingEvent-devel

This package contains library source intended for building other packages which
use the "AudioProcessingEvent" feature of the "%{crate}" crate.

%package     -n %{name}+AudioSampleFormat-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioSampleFormat-devel

This package contains library source intended for building other packages which
use the "AudioSampleFormat" feature of the "%{crate}" crate.

%package     -n %{name}+AudioScheduledSourceNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioScheduledSourceNode-devel

This package contains library source intended for building other packages which
use the "AudioScheduledSourceNode" feature of the "%{crate}" crate.

%package     -n %{name}+AudioSinkInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioSinkInfo-devel

This package contains library source intended for building other packages which
use the "AudioSinkInfo" feature of the "%{crate}" crate.

%package     -n %{name}+AudioSinkOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioSinkOptions-devel

This package contains library source intended for building other packages which
use the "AudioSinkOptions" feature of the "%{crate}" crate.

%package     -n %{name}+AudioSinkType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioSinkType-devel

This package contains library source intended for building other packages which
use the "AudioSinkType" feature of the "%{crate}" crate.

%package     -n %{name}+AudioStreamTrack-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioStreamTrack-devel

This package contains library source intended for building other packages which
use the "AudioStreamTrack" feature of the "%{crate}" crate.

%package     -n %{name}+AudioTrack-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioTrack-devel

This package contains library source intended for building other packages which
use the "AudioTrack" feature of the "%{crate}" crate.

%package     -n %{name}+AudioTrackList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioTrackList-devel

This package contains library source intended for building other packages which
use the "AudioTrackList" feature of the "%{crate}" crate.

%package     -n %{name}+AudioWorklet-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioWorklet-devel

This package contains library source intended for building other packages which
use the "AudioWorklet" feature of the "%{crate}" crate.

%package     -n %{name}+AudioWorkletGlobalScope-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioWorkletGlobalScope-devel

This package contains library source intended for building other packages which
use the "AudioWorkletGlobalScope" feature of the "%{crate}" crate.

%package     -n %{name}+AudioWorkletNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioWorkletNode-devel

This package contains library source intended for building other packages which
use the "AudioWorkletNode" feature of the "%{crate}" crate.

%package     -n %{name}+AudioWorkletNodeOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioWorkletNodeOptions-devel

This package contains library source intended for building other packages which
use the "AudioWorkletNodeOptions" feature of the "%{crate}" crate.

%package     -n %{name}+AudioWorkletProcessor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AudioWorkletProcessor-devel

This package contains library source intended for building other packages which
use the "AudioWorkletProcessor" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticationExtensionsClientInputs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticationExtensionsClientInputs-devel

This package contains library source intended for building other packages which
use the "AuthenticationExtensionsClientInputs" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticationExtensionsClientInputsJson-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticationExtensionsClientInputsJson-devel

This package contains library source intended for building other packages which
use the "AuthenticationExtensionsClientInputsJson" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticationExtensionsClientOutputs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticationExtensionsClientOutputs-devel

This package contains library source intended for building other packages which
use the "AuthenticationExtensionsClientOutputs" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticationExtensionsClientOutputsJson-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticationExtensionsClientOutputsJson-devel

This package contains library source intended for building other packages which
use the "AuthenticationExtensionsClientOutputsJson" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticationExtensionsDevicePublicKeyInputs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticationExtensionsDevicePublicKeyInputs-devel

This package contains library source intended for building other packages which
use the "AuthenticationExtensionsDevicePublicKeyInputs" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticationExtensionsDevicePublicKeyOutputs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticationExtensionsDevicePublicKeyOutputs-devel

This package contains library source intended for building other packages which
use the "AuthenticationExtensionsDevicePublicKeyOutputs" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticationExtensionsLargeBlobInputs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticationExtensionsLargeBlobInputs-devel

This package contains library source intended for building other packages which
use the "AuthenticationExtensionsLargeBlobInputs" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticationExtensionsLargeBlobOutputs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticationExtensionsLargeBlobOutputs-devel

This package contains library source intended for building other packages which
use the "AuthenticationExtensionsLargeBlobOutputs" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticationExtensionsPrfInputs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticationExtensionsPrfInputs-devel

This package contains library source intended for building other packages which
use the "AuthenticationExtensionsPrfInputs" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticationExtensionsPrfOutputs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticationExtensionsPrfOutputs-devel

This package contains library source intended for building other packages which
use the "AuthenticationExtensionsPrfOutputs" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticationExtensionsPrfValues-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticationExtensionsPrfValues-devel

This package contains library source intended for building other packages which
use the "AuthenticationExtensionsPrfValues" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticationResponseJson-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticationResponseJson-devel

This package contains library source intended for building other packages which
use the "AuthenticationResponseJson" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticatorAssertionResponse-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticatorAssertionResponse-devel

This package contains library source intended for building other packages which
use the "AuthenticatorAssertionResponse" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticatorAssertionResponseJson-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticatorAssertionResponseJson-devel

This package contains library source intended for building other packages which
use the "AuthenticatorAssertionResponseJson" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticatorAttachment-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticatorAttachment-devel

This package contains library source intended for building other packages which
use the "AuthenticatorAttachment" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticatorAttestationResponse-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticatorAttestationResponse-devel

This package contains library source intended for building other packages which
use the "AuthenticatorAttestationResponse" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticatorAttestationResponseJson-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticatorAttestationResponseJson-devel

This package contains library source intended for building other packages which
use the "AuthenticatorAttestationResponseJson" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticatorResponse-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticatorResponse-devel

This package contains library source intended for building other packages which
use the "AuthenticatorResponse" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticatorSelectionCriteria-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticatorSelectionCriteria-devel

This package contains library source intended for building other packages which
use the "AuthenticatorSelectionCriteria" feature of the "%{crate}" crate.

%package     -n %{name}+AuthenticatorTransport-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AuthenticatorTransport-devel

This package contains library source intended for building other packages which
use the "AuthenticatorTransport" feature of the "%{crate}" crate.

%package     -n %{name}+AutoKeyword-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AutoKeyword-devel

This package contains library source intended for building other packages which
use the "AutoKeyword" feature of the "%{crate}" crate.

%package     -n %{name}+AutocompleteInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+AutocompleteInfo-devel

This package contains library source intended for building other packages which
use the "AutocompleteInfo" feature of the "%{crate}" crate.

%package     -n %{name}+BarProp-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BarProp-devel

This package contains library source intended for building other packages which
use the "BarProp" feature of the "%{crate}" crate.

%package     -n %{name}+BaseAudioContext-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BaseAudioContext-devel

This package contains library source intended for building other packages which
use the "BaseAudioContext" feature of the "%{crate}" crate.

%package     -n %{name}+BaseComputedKeyframe-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BaseComputedKeyframe-devel

This package contains library source intended for building other packages which
use the "BaseComputedKeyframe" feature of the "%{crate}" crate.

%package     -n %{name}+BaseKeyframe-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BaseKeyframe-devel

This package contains library source intended for building other packages which
use the "BaseKeyframe" feature of the "%{crate}" crate.

%package     -n %{name}+BasePropertyIndexedKeyframe-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BasePropertyIndexedKeyframe-devel

This package contains library source intended for building other packages which
use the "BasePropertyIndexedKeyframe" feature of the "%{crate}" crate.

%package     -n %{name}+BasicCardRequest-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BasicCardRequest-devel

This package contains library source intended for building other packages which
use the "BasicCardRequest" feature of the "%{crate}" crate.

%package     -n %{name}+BasicCardResponse-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BasicCardResponse-devel

This package contains library source intended for building other packages which
use the "BasicCardResponse" feature of the "%{crate}" crate.

%package     -n %{name}+BasicCardType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BasicCardType-devel

This package contains library source intended for building other packages which
use the "BasicCardType" feature of the "%{crate}" crate.

%package     -n %{name}+BatteryManager-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BatteryManager-devel

This package contains library source intended for building other packages which
use the "BatteryManager" feature of the "%{crate}" crate.

%package     -n %{name}+BeforeUnloadEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BeforeUnloadEvent-devel

This package contains library source intended for building other packages which
use the "BeforeUnloadEvent" feature of the "%{crate}" crate.

%package     -n %{name}+BinaryType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BinaryType-devel

This package contains library source intended for building other packages which
use the "BinaryType" feature of the "%{crate}" crate.

%package     -n %{name}+BiquadFilterNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BiquadFilterNode-devel

This package contains library source intended for building other packages which
use the "BiquadFilterNode" feature of the "%{crate}" crate.

%package     -n %{name}+BiquadFilterOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BiquadFilterOptions-devel

This package contains library source intended for building other packages which
use the "BiquadFilterOptions" feature of the "%{crate}" crate.

%package     -n %{name}+BiquadFilterType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BiquadFilterType-devel

This package contains library source intended for building other packages which
use the "BiquadFilterType" feature of the "%{crate}" crate.

%package     -n %{name}+BitrateMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BitrateMode-devel

This package contains library source intended for building other packages which
use the "BitrateMode" feature of the "%{crate}" crate.

%package     -n %{name}+Blob-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Blob-devel

This package contains library source intended for building other packages which
use the "Blob" feature of the "%{crate}" crate.

%package     -n %{name}+BlobEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BlobEvent-devel

This package contains library source intended for building other packages which
use the "BlobEvent" feature of the "%{crate}" crate.

%package     -n %{name}+BlobEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BlobEventInit-devel

This package contains library source intended for building other packages which
use the "BlobEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+BlobPropertyBag-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BlobPropertyBag-devel

This package contains library source intended for building other packages which
use the "BlobPropertyBag" feature of the "%{crate}" crate.

%package     -n %{name}+BlockParsingOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BlockParsingOptions-devel

This package contains library source intended for building other packages which
use the "BlockParsingOptions" feature of the "%{crate}" crate.

%package     -n %{name}+Bluetooth-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Bluetooth-devel

This package contains library source intended for building other packages which
use the "Bluetooth" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothAdvertisingEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothAdvertisingEvent-devel

This package contains library source intended for building other packages which
use the "BluetoothAdvertisingEvent" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothAdvertisingEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothAdvertisingEventInit-devel

This package contains library source intended for building other packages which
use the "BluetoothAdvertisingEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothCharacteristicProperties-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothCharacteristicProperties-devel

This package contains library source intended for building other packages which
use the "BluetoothCharacteristicProperties" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothDataFilterInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothDataFilterInit-devel

This package contains library source intended for building other packages which
use the "BluetoothDataFilterInit" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothDevice-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothDevice-devel

This package contains library source intended for building other packages which
use the "BluetoothDevice" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothLeScanFilterInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothLeScanFilterInit-devel

This package contains library source intended for building other packages which
use the "BluetoothLeScanFilterInit" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothManufacturerDataMap-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothManufacturerDataMap-devel

This package contains library source intended for building other packages which
use the "BluetoothManufacturerDataMap" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothPermissionDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothPermissionDescriptor-devel

This package contains library source intended for building other packages which
use the "BluetoothPermissionDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothPermissionResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothPermissionResult-devel

This package contains library source intended for building other packages which
use the "BluetoothPermissionResult" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothPermissionStorage-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothPermissionStorage-devel

This package contains library source intended for building other packages which
use the "BluetoothPermissionStorage" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothRemoteGattCharacteristic-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothRemoteGattCharacteristic-devel

This package contains library source intended for building other packages which
use the "BluetoothRemoteGattCharacteristic" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothRemoteGattDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothRemoteGattDescriptor-devel

This package contains library source intended for building other packages which
use the "BluetoothRemoteGattDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothRemoteGattServer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothRemoteGattServer-devel

This package contains library source intended for building other packages which
use the "BluetoothRemoteGattServer" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothRemoteGattService-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothRemoteGattService-devel

This package contains library source intended for building other packages which
use the "BluetoothRemoteGattService" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothServiceDataMap-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothServiceDataMap-devel

This package contains library source intended for building other packages which
use the "BluetoothServiceDataMap" feature of the "%{crate}" crate.

%package     -n %{name}+BluetoothUuid-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BluetoothUuid-devel

This package contains library source intended for building other packages which
use the "BluetoothUuid" feature of the "%{crate}" crate.

%package     -n %{name}+BoxQuadOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BoxQuadOptions-devel

This package contains library source intended for building other packages which
use the "BoxQuadOptions" feature of the "%{crate}" crate.

%package     -n %{name}+BroadcastChannel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BroadcastChannel-devel

This package contains library source intended for building other packages which
use the "BroadcastChannel" feature of the "%{crate}" crate.

%package     -n %{name}+BrowserElementDownloadOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BrowserElementDownloadOptions-devel

This package contains library source intended for building other packages which
use the "BrowserElementDownloadOptions" feature of the "%{crate}" crate.

%package     -n %{name}+BrowserElementExecuteScriptOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BrowserElementExecuteScriptOptions-devel

This package contains library source intended for building other packages which
use the "BrowserElementExecuteScriptOptions" feature of the "%{crate}" crate.

%package     -n %{name}+BrowserFeedWriter-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BrowserFeedWriter-devel

This package contains library source intended for building other packages which
use the "BrowserFeedWriter" feature of the "%{crate}" crate.

%package     -n %{name}+BrowserFindCaseSensitivity-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BrowserFindCaseSensitivity-devel

This package contains library source intended for building other packages which
use the "BrowserFindCaseSensitivity" feature of the "%{crate}" crate.

%package     -n %{name}+BrowserFindDirection-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+BrowserFindDirection-devel

This package contains library source intended for building other packages which
use the "BrowserFindDirection" feature of the "%{crate}" crate.

%package     -n %{name}+ByteLengthQueuingStrategy-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ByteLengthQueuingStrategy-devel

This package contains library source intended for building other packages which
use the "ByteLengthQueuingStrategy" feature of the "%{crate}" crate.

%package     -n %{name}+Cache-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Cache-devel

This package contains library source intended for building other packages which
use the "Cache" feature of the "%{crate}" crate.

%package     -n %{name}+CacheBatchOperation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CacheBatchOperation-devel

This package contains library source intended for building other packages which
use the "CacheBatchOperation" feature of the "%{crate}" crate.

%package     -n %{name}+CacheQueryOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CacheQueryOptions-devel

This package contains library source intended for building other packages which
use the "CacheQueryOptions" feature of the "%{crate}" crate.

%package     -n %{name}+CacheStorage-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CacheStorage-devel

This package contains library source intended for building other packages which
use the "CacheStorage" feature of the "%{crate}" crate.

%package     -n %{name}+CacheStorageNamespace-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CacheStorageNamespace-devel

This package contains library source intended for building other packages which
use the "CacheStorageNamespace" feature of the "%{crate}" crate.

%package     -n %{name}+CanvasCaptureMediaStream-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CanvasCaptureMediaStream-devel

This package contains library source intended for building other packages which
use the "CanvasCaptureMediaStream" feature of the "%{crate}" crate.

%package     -n %{name}+CanvasCaptureMediaStreamTrack-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CanvasCaptureMediaStreamTrack-devel

This package contains library source intended for building other packages which
use the "CanvasCaptureMediaStreamTrack" feature of the "%{crate}" crate.

%package     -n %{name}+CanvasGradient-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CanvasGradient-devel

This package contains library source intended for building other packages which
use the "CanvasGradient" feature of the "%{crate}" crate.

%package     -n %{name}+CanvasPattern-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CanvasPattern-devel

This package contains library source intended for building other packages which
use the "CanvasPattern" feature of the "%{crate}" crate.

%package     -n %{name}+CanvasRenderingContext2d-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CanvasRenderingContext2d-devel

This package contains library source intended for building other packages which
use the "CanvasRenderingContext2d" feature of the "%{crate}" crate.

%package     -n %{name}+CanvasWindingRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CanvasWindingRule-devel

This package contains library source intended for building other packages which
use the "CanvasWindingRule" feature of the "%{crate}" crate.

%package     -n %{name}+CaretChangedReason-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CaretChangedReason-devel

This package contains library source intended for building other packages which
use the "CaretChangedReason" feature of the "%{crate}" crate.

%package     -n %{name}+CaretPosition-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CaretPosition-devel

This package contains library source intended for building other packages which
use the "CaretPosition" feature of the "%{crate}" crate.

%package     -n %{name}+CaretStateChangedEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CaretStateChangedEventInit-devel

This package contains library source intended for building other packages which
use the "CaretStateChangedEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+CdataSection-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CdataSection-devel

This package contains library source intended for building other packages which
use the "CdataSection" feature of the "%{crate}" crate.

%package     -n %{name}+ChannelCountMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ChannelCountMode-devel

This package contains library source intended for building other packages which
use the "ChannelCountMode" feature of the "%{crate}" crate.

%package     -n %{name}+ChannelInterpretation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ChannelInterpretation-devel

This package contains library source intended for building other packages which
use the "ChannelInterpretation" feature of the "%{crate}" crate.

%package     -n %{name}+ChannelMergerNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ChannelMergerNode-devel

This package contains library source intended for building other packages which
use the "ChannelMergerNode" feature of the "%{crate}" crate.

%package     -n %{name}+ChannelMergerOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ChannelMergerOptions-devel

This package contains library source intended for building other packages which
use the "ChannelMergerOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ChannelSplitterNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ChannelSplitterNode-devel

This package contains library source intended for building other packages which
use the "ChannelSplitterNode" feature of the "%{crate}" crate.

%package     -n %{name}+ChannelSplitterOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ChannelSplitterOptions-devel

This package contains library source intended for building other packages which
use the "ChannelSplitterOptions" feature of the "%{crate}" crate.

%package     -n %{name}+CharacterData-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CharacterData-devel

This package contains library source intended for building other packages which
use the "CharacterData" feature of the "%{crate}" crate.

%package     -n %{name}+CheckerboardReason-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CheckerboardReason-devel

This package contains library source intended for building other packages which
use the "CheckerboardReason" feature of the "%{crate}" crate.

%package     -n %{name}+CheckerboardReport-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CheckerboardReport-devel

This package contains library source intended for building other packages which
use the "CheckerboardReport" feature of the "%{crate}" crate.

%package     -n %{name}+CheckerboardReportService-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CheckerboardReportService-devel

This package contains library source intended for building other packages which
use the "CheckerboardReportService" feature of the "%{crate}" crate.

%package     -n %{name}+ChromeFilePropertyBag-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ChromeFilePropertyBag-devel

This package contains library source intended for building other packages which
use the "ChromeFilePropertyBag" feature of the "%{crate}" crate.

%package     -n %{name}+ChromeWorker-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ChromeWorker-devel

This package contains library source intended for building other packages which
use the "ChromeWorker" feature of the "%{crate}" crate.

%package     -n %{name}+Client-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Client-devel

This package contains library source intended for building other packages which
use the "Client" feature of the "%{crate}" crate.

%package     -n %{name}+ClientQueryOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ClientQueryOptions-devel

This package contains library source intended for building other packages which
use the "ClientQueryOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ClientRectsAndTexts-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ClientRectsAndTexts-devel

This package contains library source intended for building other packages which
use the "ClientRectsAndTexts" feature of the "%{crate}" crate.

%package     -n %{name}+ClientType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ClientType-devel

This package contains library source intended for building other packages which
use the "ClientType" feature of the "%{crate}" crate.

%package     -n %{name}+Clients-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Clients-devel

This package contains library source intended for building other packages which
use the "Clients" feature of the "%{crate}" crate.

%package     -n %{name}+Clipboard-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Clipboard-devel

This package contains library source intended for building other packages which
use the "Clipboard" feature of the "%{crate}" crate.

%package     -n %{name}+ClipboardEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ClipboardEvent-devel

This package contains library source intended for building other packages which
use the "ClipboardEvent" feature of the "%{crate}" crate.

%package     -n %{name}+ClipboardEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ClipboardEventInit-devel

This package contains library source intended for building other packages which
use the "ClipboardEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+ClipboardItem-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ClipboardItem-devel

This package contains library source intended for building other packages which
use the "ClipboardItem" feature of the "%{crate}" crate.

%package     -n %{name}+ClipboardItemOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ClipboardItemOptions-devel

This package contains library source intended for building other packages which
use the "ClipboardItemOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ClipboardPermissionDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ClipboardPermissionDescriptor-devel

This package contains library source intended for building other packages which
use the "ClipboardPermissionDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+ClipboardUnsanitizedFormats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ClipboardUnsanitizedFormats-devel

This package contains library source intended for building other packages which
use the "ClipboardUnsanitizedFormats" feature of the "%{crate}" crate.

%package     -n %{name}+CloseEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CloseEvent-devel

This package contains library source intended for building other packages which
use the "CloseEvent" feature of the "%{crate}" crate.

%package     -n %{name}+CloseEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CloseEventInit-devel

This package contains library source intended for building other packages which
use the "CloseEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+CodecState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CodecState-devel

This package contains library source intended for building other packages which
use the "CodecState" feature of the "%{crate}" crate.

%package     -n %{name}+CollectedClientData-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CollectedClientData-devel

This package contains library source intended for building other packages which
use the "CollectedClientData" feature of the "%{crate}" crate.

%package     -n %{name}+ColorSpaceConversion-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ColorSpaceConversion-devel

This package contains library source intended for building other packages which
use the "ColorSpaceConversion" feature of the "%{crate}" crate.

%package     -n %{name}+CommandEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CommandEvent-devel

This package contains library source intended for building other packages which
use the "CommandEvent" feature of the "%{crate}" crate.

%package     -n %{name}+CommandEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CommandEventInit-devel

This package contains library source intended for building other packages which
use the "CommandEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+Comment-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Comment-devel

This package contains library source intended for building other packages which
use the "Comment" feature of the "%{crate}" crate.

%package     -n %{name}+CompositeOperation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CompositeOperation-devel

This package contains library source intended for building other packages which
use the "CompositeOperation" feature of the "%{crate}" crate.

%package     -n %{name}+CompositionEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CompositionEvent-devel

This package contains library source intended for building other packages which
use the "CompositionEvent" feature of the "%{crate}" crate.

%package     -n %{name}+CompositionEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CompositionEventInit-devel

This package contains library source intended for building other packages which
use the "CompositionEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+CompressionFormat-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CompressionFormat-devel

This package contains library source intended for building other packages which
use the "CompressionFormat" feature of the "%{crate}" crate.

%package     -n %{name}+CompressionStream-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CompressionStream-devel

This package contains library source intended for building other packages which
use the "CompressionStream" feature of the "%{crate}" crate.

%package     -n %{name}+ComputedEffectTiming-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ComputedEffectTiming-devel

This package contains library source intended for building other packages which
use the "ComputedEffectTiming" feature of the "%{crate}" crate.

%package     -n %{name}+ConnStatusDict-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConnStatusDict-devel

This package contains library source intended for building other packages which
use the "ConnStatusDict" feature of the "%{crate}" crate.

%package     -n %{name}+ConnectionType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConnectionType-devel

This package contains library source intended for building other packages which
use the "ConnectionType" feature of the "%{crate}" crate.

%package     -n %{name}+ConsoleCounter-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConsoleCounter-devel

This package contains library source intended for building other packages which
use the "ConsoleCounter" feature of the "%{crate}" crate.

%package     -n %{name}+ConsoleCounterError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConsoleCounterError-devel

This package contains library source intended for building other packages which
use the "ConsoleCounterError" feature of the "%{crate}" crate.

%package     -n %{name}+ConsoleEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConsoleEvent-devel

This package contains library source intended for building other packages which
use the "ConsoleEvent" feature of the "%{crate}" crate.

%package     -n %{name}+ConsoleInstance-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConsoleInstance-devel

This package contains library source intended for building other packages which
use the "ConsoleInstance" feature of the "%{crate}" crate.

%package     -n %{name}+ConsoleInstanceOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConsoleInstanceOptions-devel

This package contains library source intended for building other packages which
use the "ConsoleInstanceOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ConsoleLevel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConsoleLevel-devel

This package contains library source intended for building other packages which
use the "ConsoleLevel" feature of the "%{crate}" crate.

%package     -n %{name}+ConsoleLogLevel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConsoleLogLevel-devel

This package contains library source intended for building other packages which
use the "ConsoleLogLevel" feature of the "%{crate}" crate.

%package     -n %{name}+ConsoleProfileEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConsoleProfileEvent-devel

This package contains library source intended for building other packages which
use the "ConsoleProfileEvent" feature of the "%{crate}" crate.

%package     -n %{name}+ConsoleStackEntry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConsoleStackEntry-devel

This package contains library source intended for building other packages which
use the "ConsoleStackEntry" feature of the "%{crate}" crate.

%package     -n %{name}+ConsoleTimerError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConsoleTimerError-devel

This package contains library source intended for building other packages which
use the "ConsoleTimerError" feature of the "%{crate}" crate.

%package     -n %{name}+ConsoleTimerLogOrEnd-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConsoleTimerLogOrEnd-devel

This package contains library source intended for building other packages which
use the "ConsoleTimerLogOrEnd" feature of the "%{crate}" crate.

%package     -n %{name}+ConsoleTimerStart-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConsoleTimerStart-devel

This package contains library source intended for building other packages which
use the "ConsoleTimerStart" feature of the "%{crate}" crate.

%package     -n %{name}+ConstantSourceNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConstantSourceNode-devel

This package contains library source intended for building other packages which
use the "ConstantSourceNode" feature of the "%{crate}" crate.

%package     -n %{name}+ConstantSourceOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConstantSourceOptions-devel

This package contains library source intended for building other packages which
use the "ConstantSourceOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ConstrainBooleanParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConstrainBooleanParameters-devel

This package contains library source intended for building other packages which
use the "ConstrainBooleanParameters" feature of the "%{crate}" crate.

%package     -n %{name}+ConstrainDomStringParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConstrainDomStringParameters-devel

This package contains library source intended for building other packages which
use the "ConstrainDomStringParameters" feature of the "%{crate}" crate.

%package     -n %{name}+ConstrainDoubleRange-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConstrainDoubleRange-devel

This package contains library source intended for building other packages which
use the "ConstrainDoubleRange" feature of the "%{crate}" crate.

%package     -n %{name}+ConstrainLongRange-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConstrainLongRange-devel

This package contains library source intended for building other packages which
use the "ConstrainLongRange" feature of the "%{crate}" crate.

%package     -n %{name}+ContextAttributes2d-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ContextAttributes2d-devel

This package contains library source intended for building other packages which
use the "ContextAttributes2d" feature of the "%{crate}" crate.

%package     -n %{name}+ConvertCoordinateOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConvertCoordinateOptions-devel

This package contains library source intended for building other packages which
use the "ConvertCoordinateOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ConvolverNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConvolverNode-devel

This package contains library source intended for building other packages which
use the "ConvolverNode" feature of the "%{crate}" crate.

%package     -n %{name}+ConvolverOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ConvolverOptions-devel

This package contains library source intended for building other packages which
use the "ConvolverOptions" feature of the "%{crate}" crate.

%package     -n %{name}+CookieChangeEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CookieChangeEvent-devel

This package contains library source intended for building other packages which
use the "CookieChangeEvent" feature of the "%{crate}" crate.

%package     -n %{name}+CookieChangeEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CookieChangeEventInit-devel

This package contains library source intended for building other packages which
use the "CookieChangeEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+CookieInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CookieInit-devel

This package contains library source intended for building other packages which
use the "CookieInit" feature of the "%{crate}" crate.

%package     -n %{name}+CookieListItem-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CookieListItem-devel

This package contains library source intended for building other packages which
use the "CookieListItem" feature of the "%{crate}" crate.

%package     -n %{name}+CookieSameSite-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CookieSameSite-devel

This package contains library source intended for building other packages which
use the "CookieSameSite" feature of the "%{crate}" crate.

%package     -n %{name}+CookieStore-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CookieStore-devel

This package contains library source intended for building other packages which
use the "CookieStore" feature of the "%{crate}" crate.

%package     -n %{name}+CookieStoreDeleteOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CookieStoreDeleteOptions-devel

This package contains library source intended for building other packages which
use the "CookieStoreDeleteOptions" feature of the "%{crate}" crate.

%package     -n %{name}+CookieStoreGetOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CookieStoreGetOptions-devel

This package contains library source intended for building other packages which
use the "CookieStoreGetOptions" feature of the "%{crate}" crate.

%package     -n %{name}+CookieStoreManager-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CookieStoreManager-devel

This package contains library source intended for building other packages which
use the "CookieStoreManager" feature of the "%{crate}" crate.

%package     -n %{name}+Coordinates-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Coordinates-devel

This package contains library source intended for building other packages which
use the "Coordinates" feature of the "%{crate}" crate.

%package     -n %{name}+CountQueuingStrategy-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CountQueuingStrategy-devel

This package contains library source intended for building other packages which
use the "CountQueuingStrategy" feature of the "%{crate}" crate.

%package     -n %{name}+Credential-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Credential-devel

This package contains library source intended for building other packages which
use the "Credential" feature of the "%{crate}" crate.

%package     -n %{name}+CredentialCreationOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CredentialCreationOptions-devel

This package contains library source intended for building other packages which
use the "CredentialCreationOptions" feature of the "%{crate}" crate.

%package     -n %{name}+CredentialPropertiesOutput-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CredentialPropertiesOutput-devel

This package contains library source intended for building other packages which
use the "CredentialPropertiesOutput" feature of the "%{crate}" crate.

%package     -n %{name}+CredentialRequestOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CredentialRequestOptions-devel

This package contains library source intended for building other packages which
use the "CredentialRequestOptions" feature of the "%{crate}" crate.

%package     -n %{name}+CredentialsContainer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CredentialsContainer-devel

This package contains library source intended for building other packages which
use the "CredentialsContainer" feature of the "%{crate}" crate.

%package     -n %{name}+Crypto-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Crypto-devel

This package contains library source intended for building other packages which
use the "Crypto" feature of the "%{crate}" crate.

%package     -n %{name}+CryptoKey-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CryptoKey-devel

This package contains library source intended for building other packages which
use the "CryptoKey" feature of the "%{crate}" crate.

%package     -n %{name}+CryptoKeyPair-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CryptoKeyPair-devel

This package contains library source intended for building other packages which
use the "CryptoKeyPair" feature of the "%{crate}" crate.

%package     -n %{name}+CssAnimation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssAnimation-devel

This package contains library source intended for building other packages which
use the "CssAnimation" feature of the "%{crate}" crate.

%package     -n %{name}+CssBoxType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssBoxType-devel

This package contains library source intended for building other packages which
use the "CssBoxType" feature of the "%{crate}" crate.

%package     -n %{name}+CssConditionRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssConditionRule-devel

This package contains library source intended for building other packages which
use the "CssConditionRule" feature of the "%{crate}" crate.

%package     -n %{name}+CssCounterStyleRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssCounterStyleRule-devel

This package contains library source intended for building other packages which
use the "CssCounterStyleRule" feature of the "%{crate}" crate.

%package     -n %{name}+CssFontFaceRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssFontFaceRule-devel

This package contains library source intended for building other packages which
use the "CssFontFaceRule" feature of the "%{crate}" crate.

%package     -n %{name}+CssFontFeatureValuesRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssFontFeatureValuesRule-devel

This package contains library source intended for building other packages which
use the "CssFontFeatureValuesRule" feature of the "%{crate}" crate.

%package     -n %{name}+CssGroupingRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssGroupingRule-devel

This package contains library source intended for building other packages which
use the "CssGroupingRule" feature of the "%{crate}" crate.

%package     -n %{name}+CssImportRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssImportRule-devel

This package contains library source intended for building other packages which
use the "CssImportRule" feature of the "%{crate}" crate.

%package     -n %{name}+CssKeyframeRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssKeyframeRule-devel

This package contains library source intended for building other packages which
use the "CssKeyframeRule" feature of the "%{crate}" crate.

%package     -n %{name}+CssKeyframesRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssKeyframesRule-devel

This package contains library source intended for building other packages which
use the "CssKeyframesRule" feature of the "%{crate}" crate.

%package     -n %{name}+CssMediaRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssMediaRule-devel

This package contains library source intended for building other packages which
use the "CssMediaRule" feature of the "%{crate}" crate.

%package     -n %{name}+CssNamespaceRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssNamespaceRule-devel

This package contains library source intended for building other packages which
use the "CssNamespaceRule" feature of the "%{crate}" crate.

%package     -n %{name}+CssPageRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssPageRule-devel

This package contains library source intended for building other packages which
use the "CssPageRule" feature of the "%{crate}" crate.

%package     -n %{name}+CssPseudoElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssPseudoElement-devel

This package contains library source intended for building other packages which
use the "CssPseudoElement" feature of the "%{crate}" crate.

%package     -n %{name}+CssRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssRule-devel

This package contains library source intended for building other packages which
use the "CssRule" feature of the "%{crate}" crate.

%package     -n %{name}+CssRuleList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssRuleList-devel

This package contains library source intended for building other packages which
use the "CssRuleList" feature of the "%{crate}" crate.

%package     -n %{name}+CssStyleDeclaration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssStyleDeclaration-devel

This package contains library source intended for building other packages which
use the "CssStyleDeclaration" feature of the "%{crate}" crate.

%package     -n %{name}+CssStyleRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssStyleRule-devel

This package contains library source intended for building other packages which
use the "CssStyleRule" feature of the "%{crate}" crate.

%package     -n %{name}+CssStyleSheet-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssStyleSheet-devel

This package contains library source intended for building other packages which
use the "CssStyleSheet" feature of the "%{crate}" crate.

%package     -n %{name}+CssStyleSheetParsingMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssStyleSheetParsingMode-devel

This package contains library source intended for building other packages which
use the "CssStyleSheetParsingMode" feature of the "%{crate}" crate.

%package     -n %{name}+CssSupportsRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssSupportsRule-devel

This package contains library source intended for building other packages which
use the "CssSupportsRule" feature of the "%{crate}" crate.

%package     -n %{name}+CssTransition-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssTransition-devel

This package contains library source intended for building other packages which
use the "CssTransition" feature of the "%{crate}" crate.

%package     -n %{name}+CssViewTransitionRule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CssViewTransitionRule-devel

This package contains library source intended for building other packages which
use the "CssViewTransitionRule" feature of the "%{crate}" crate.

%package     -n %{name}+CustomElementRegistry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CustomElementRegistry-devel

This package contains library source intended for building other packages which
use the "CustomElementRegistry" feature of the "%{crate}" crate.

%package     -n %{name}+CustomEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CustomEvent-devel

This package contains library source intended for building other packages which
use the "CustomEvent" feature of the "%{crate}" crate.

%package     -n %{name}+CustomEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+CustomEventInit-devel

This package contains library source intended for building other packages which
use the "CustomEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+DataTransfer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DataTransfer-devel

This package contains library source intended for building other packages which
use the "DataTransfer" feature of the "%{crate}" crate.

%package     -n %{name}+DataTransferItem-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DataTransferItem-devel

This package contains library source intended for building other packages which
use the "DataTransferItem" feature of the "%{crate}" crate.

%package     -n %{name}+DataTransferItemList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DataTransferItemList-devel

This package contains library source intended for building other packages which
use the "DataTransferItemList" feature of the "%{crate}" crate.

%package     -n %{name}+DateTimeValue-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DateTimeValue-devel

This package contains library source intended for building other packages which
use the "DateTimeValue" feature of the "%{crate}" crate.

%package     -n %{name}+DecoderDoctorNotification-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DecoderDoctorNotification-devel

This package contains library source intended for building other packages which
use the "DecoderDoctorNotification" feature of the "%{crate}" crate.

%package     -n %{name}+DecoderDoctorNotificationType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DecoderDoctorNotificationType-devel

This package contains library source intended for building other packages which
use the "DecoderDoctorNotificationType" feature of the "%{crate}" crate.

%package     -n %{name}+DecompressionStream-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DecompressionStream-devel

This package contains library source intended for building other packages which
use the "DecompressionStream" feature of the "%{crate}" crate.

%package     -n %{name}+DedicatedWorkerGlobalScope-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DedicatedWorkerGlobalScope-devel

This package contains library source intended for building other packages which
use the "DedicatedWorkerGlobalScope" feature of the "%{crate}" crate.

%package     -n %{name}+DelayNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DelayNode-devel

This package contains library source intended for building other packages which
use the "DelayNode" feature of the "%{crate}" crate.

%package     -n %{name}+DelayOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DelayOptions-devel

This package contains library source intended for building other packages which
use the "DelayOptions" feature of the "%{crate}" crate.

%package     -n %{name}+DeviceAcceleration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DeviceAcceleration-devel

This package contains library source intended for building other packages which
use the "DeviceAcceleration" feature of the "%{crate}" crate.

%package     -n %{name}+DeviceAccelerationInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DeviceAccelerationInit-devel

This package contains library source intended for building other packages which
use the "DeviceAccelerationInit" feature of the "%{crate}" crate.

%package     -n %{name}+DeviceLightEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DeviceLightEvent-devel

This package contains library source intended for building other packages which
use the "DeviceLightEvent" feature of the "%{crate}" crate.

%package     -n %{name}+DeviceLightEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DeviceLightEventInit-devel

This package contains library source intended for building other packages which
use the "DeviceLightEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+DeviceMotionEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DeviceMotionEvent-devel

This package contains library source intended for building other packages which
use the "DeviceMotionEvent" feature of the "%{crate}" crate.

%package     -n %{name}+DeviceMotionEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DeviceMotionEventInit-devel

This package contains library source intended for building other packages which
use the "DeviceMotionEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+DeviceOrientationEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DeviceOrientationEvent-devel

This package contains library source intended for building other packages which
use the "DeviceOrientationEvent" feature of the "%{crate}" crate.

%package     -n %{name}+DeviceOrientationEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DeviceOrientationEventInit-devel

This package contains library source intended for building other packages which
use the "DeviceOrientationEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+DeviceProximityEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DeviceProximityEvent-devel

This package contains library source intended for building other packages which
use the "DeviceProximityEvent" feature of the "%{crate}" crate.

%package     -n %{name}+DeviceProximityEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DeviceProximityEventInit-devel

This package contains library source intended for building other packages which
use the "DeviceProximityEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+DeviceRotationRate-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DeviceRotationRate-devel

This package contains library source intended for building other packages which
use the "DeviceRotationRate" feature of the "%{crate}" crate.

%package     -n %{name}+DeviceRotationRateInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DeviceRotationRateInit-devel

This package contains library source intended for building other packages which
use the "DeviceRotationRateInit" feature of the "%{crate}" crate.

%package     -n %{name}+DhKeyDeriveParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DhKeyDeriveParams-devel

This package contains library source intended for building other packages which
use the "DhKeyDeriveParams" feature of the "%{crate}" crate.

%package     -n %{name}+DirectionSetting-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DirectionSetting-devel

This package contains library source intended for building other packages which
use the "DirectionSetting" feature of the "%{crate}" crate.

%package     -n %{name}+Directory-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Directory-devel

This package contains library source intended for building other packages which
use the "Directory" feature of the "%{crate}" crate.

%package     -n %{name}+DirectoryPickerOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DirectoryPickerOptions-devel

This package contains library source intended for building other packages which
use the "DirectoryPickerOptions" feature of the "%{crate}" crate.

%package     -n %{name}+DisplayMediaStreamConstraints-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DisplayMediaStreamConstraints-devel

This package contains library source intended for building other packages which
use the "DisplayMediaStreamConstraints" feature of the "%{crate}" crate.

%package     -n %{name}+DisplayNameOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DisplayNameOptions-devel

This package contains library source intended for building other packages which
use the "DisplayNameOptions" feature of the "%{crate}" crate.

%package     -n %{name}+DisplayNameResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DisplayNameResult-devel

This package contains library source intended for building other packages which
use the "DisplayNameResult" feature of the "%{crate}" crate.

%package     -n %{name}+DistanceModelType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DistanceModelType-devel

This package contains library source intended for building other packages which
use the "DistanceModelType" feature of the "%{crate}" crate.

%package     -n %{name}+DnsCacheDict-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DnsCacheDict-devel

This package contains library source intended for building other packages which
use the "DnsCacheDict" feature of the "%{crate}" crate.

%package     -n %{name}+DnsCacheEntry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DnsCacheEntry-devel

This package contains library source intended for building other packages which
use the "DnsCacheEntry" feature of the "%{crate}" crate.

%package     -n %{name}+DnsLookupDict-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DnsLookupDict-devel

This package contains library source intended for building other packages which
use the "DnsLookupDict" feature of the "%{crate}" crate.

%package     -n %{name}+Document-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Document-devel

This package contains library source intended for building other packages which
use the "Document" feature of the "%{crate}" crate.

%package     -n %{name}+DocumentFragment-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DocumentFragment-devel

This package contains library source intended for building other packages which
use the "DocumentFragment" feature of the "%{crate}" crate.

%package     -n %{name}+DocumentTimeline-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DocumentTimeline-devel

This package contains library source intended for building other packages which
use the "DocumentTimeline" feature of the "%{crate}" crate.

%package     -n %{name}+DocumentTimelineOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DocumentTimelineOptions-devel

This package contains library source intended for building other packages which
use the "DocumentTimelineOptions" feature of the "%{crate}" crate.

%package     -n %{name}+DocumentType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DocumentType-devel

This package contains library source intended for building other packages which
use the "DocumentType" feature of the "%{crate}" crate.

%package     -n %{name}+DomError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomError-devel

This package contains library source intended for building other packages which
use the "DomError" feature of the "%{crate}" crate.

%package     -n %{name}+DomException-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomException-devel

This package contains library source intended for building other packages which
use the "DomException" feature of the "%{crate}" crate.

%package     -n %{name}+DomImplementation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomImplementation-devel

This package contains library source intended for building other packages which
use the "DomImplementation" feature of the "%{crate}" crate.

%package     -n %{name}+DomMatrix-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomMatrix-devel

This package contains library source intended for building other packages which
use the "DomMatrix" feature of the "%{crate}" crate.

%package     -n %{name}+DomMatrix2dInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomMatrix2dInit-devel

This package contains library source intended for building other packages which
use the "DomMatrix2dInit" feature of the "%{crate}" crate.

%package     -n %{name}+DomMatrixInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomMatrixInit-devel

This package contains library source intended for building other packages which
use the "DomMatrixInit" feature of the "%{crate}" crate.

%package     -n %{name}+DomMatrixReadOnly-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomMatrixReadOnly-devel

This package contains library source intended for building other packages which
use the "DomMatrixReadOnly" feature of the "%{crate}" crate.

%package     -n %{name}+DomParser-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomParser-devel

This package contains library source intended for building other packages which
use the "DomParser" feature of the "%{crate}" crate.

%package     -n %{name}+DomPoint-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomPoint-devel

This package contains library source intended for building other packages which
use the "DomPoint" feature of the "%{crate}" crate.

%package     -n %{name}+DomPointInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomPointInit-devel

This package contains library source intended for building other packages which
use the "DomPointInit" feature of the "%{crate}" crate.

%package     -n %{name}+DomPointReadOnly-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomPointReadOnly-devel

This package contains library source intended for building other packages which
use the "DomPointReadOnly" feature of the "%{crate}" crate.

%package     -n %{name}+DomQuad-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomQuad-devel

This package contains library source intended for building other packages which
use the "DomQuad" feature of the "%{crate}" crate.

%package     -n %{name}+DomQuadInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomQuadInit-devel

This package contains library source intended for building other packages which
use the "DomQuadInit" feature of the "%{crate}" crate.

%package     -n %{name}+DomQuadJson-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomQuadJson-devel

This package contains library source intended for building other packages which
use the "DomQuadJson" feature of the "%{crate}" crate.

%package     -n %{name}+DomRect-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomRect-devel

This package contains library source intended for building other packages which
use the "DomRect" feature of the "%{crate}" crate.

%package     -n %{name}+DomRectInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomRectInit-devel

This package contains library source intended for building other packages which
use the "DomRectInit" feature of the "%{crate}" crate.

%package     -n %{name}+DomRectList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomRectList-devel

This package contains library source intended for building other packages which
use the "DomRectList" feature of the "%{crate}" crate.

%package     -n %{name}+DomRectReadOnly-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomRectReadOnly-devel

This package contains library source intended for building other packages which
use the "DomRectReadOnly" feature of the "%{crate}" crate.

%package     -n %{name}+DomRequest-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomRequest-devel

This package contains library source intended for building other packages which
use the "DomRequest" feature of the "%{crate}" crate.

%package     -n %{name}+DomRequestReadyState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomRequestReadyState-devel

This package contains library source intended for building other packages which
use the "DomRequestReadyState" feature of the "%{crate}" crate.

%package     -n %{name}+DomStringList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomStringList-devel

This package contains library source intended for building other packages which
use the "DomStringList" feature of the "%{crate}" crate.

%package     -n %{name}+DomStringMap-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomStringMap-devel

This package contains library source intended for building other packages which
use the "DomStringMap" feature of the "%{crate}" crate.

%package     -n %{name}+DomTokenList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomTokenList-devel

This package contains library source intended for building other packages which
use the "DomTokenList" feature of the "%{crate}" crate.

%package     -n %{name}+DomWindowResizeEventDetail-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DomWindowResizeEventDetail-devel

This package contains library source intended for building other packages which
use the "DomWindowResizeEventDetail" feature of the "%{crate}" crate.

%package     -n %{name}+DoubleRange-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DoubleRange-devel

This package contains library source intended for building other packages which
use the "DoubleRange" feature of the "%{crate}" crate.

%package     -n %{name}+DragEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DragEvent-devel

This package contains library source intended for building other packages which
use the "DragEvent" feature of the "%{crate}" crate.

%package     -n %{name}+DragEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DragEventInit-devel

This package contains library source intended for building other packages which
use the "DragEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+DynamicsCompressorNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DynamicsCompressorNode-devel

This package contains library source intended for building other packages which
use the "DynamicsCompressorNode" feature of the "%{crate}" crate.

%package     -n %{name}+DynamicsCompressorOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+DynamicsCompressorOptions-devel

This package contains library source intended for building other packages which
use the "DynamicsCompressorOptions" feature of the "%{crate}" crate.

%package     -n %{name}+EcKeyAlgorithm-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EcKeyAlgorithm-devel

This package contains library source intended for building other packages which
use the "EcKeyAlgorithm" feature of the "%{crate}" crate.

%package     -n %{name}+EcKeyGenParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EcKeyGenParams-devel

This package contains library source intended for building other packages which
use the "EcKeyGenParams" feature of the "%{crate}" crate.

%package     -n %{name}+EcKeyImportParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EcKeyImportParams-devel

This package contains library source intended for building other packages which
use the "EcKeyImportParams" feature of the "%{crate}" crate.

%package     -n %{name}+EcdhKeyDeriveParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EcdhKeyDeriveParams-devel

This package contains library source intended for building other packages which
use the "EcdhKeyDeriveParams" feature of the "%{crate}" crate.

%package     -n %{name}+EcdsaParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EcdsaParams-devel

This package contains library source intended for building other packages which
use the "EcdsaParams" feature of the "%{crate}" crate.

%package     -n %{name}+EffectTiming-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EffectTiming-devel

This package contains library source intended for building other packages which
use the "EffectTiming" feature of the "%{crate}" crate.

%package     -n %{name}+Element-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Element-devel

This package contains library source intended for building other packages which
use the "Element" feature of the "%{crate}" crate.

%package     -n %{name}+ElementCreationOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ElementCreationOptions-devel

This package contains library source intended for building other packages which
use the "ElementCreationOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ElementDefinitionOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ElementDefinitionOptions-devel

This package contains library source intended for building other packages which
use the "ElementDefinitionOptions" feature of the "%{crate}" crate.

%package     -n %{name}+EncodedAudioChunk-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EncodedAudioChunk-devel

This package contains library source intended for building other packages which
use the "EncodedAudioChunk" feature of the "%{crate}" crate.

%package     -n %{name}+EncodedAudioChunkInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EncodedAudioChunkInit-devel

This package contains library source intended for building other packages which
use the "EncodedAudioChunkInit" feature of the "%{crate}" crate.

%package     -n %{name}+EncodedAudioChunkMetadata-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EncodedAudioChunkMetadata-devel

This package contains library source intended for building other packages which
use the "EncodedAudioChunkMetadata" feature of the "%{crate}" crate.

%package     -n %{name}+EncodedAudioChunkType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EncodedAudioChunkType-devel

This package contains library source intended for building other packages which
use the "EncodedAudioChunkType" feature of the "%{crate}" crate.

%package     -n %{name}+EncodedVideoChunk-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EncodedVideoChunk-devel

This package contains library source intended for building other packages which
use the "EncodedVideoChunk" feature of the "%{crate}" crate.

%package     -n %{name}+EncodedVideoChunkInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EncodedVideoChunkInit-devel

This package contains library source intended for building other packages which
use the "EncodedVideoChunkInit" feature of the "%{crate}" crate.

%package     -n %{name}+EncodedVideoChunkMetadata-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EncodedVideoChunkMetadata-devel

This package contains library source intended for building other packages which
use the "EncodedVideoChunkMetadata" feature of the "%{crate}" crate.

%package     -n %{name}+EncodedVideoChunkType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EncodedVideoChunkType-devel

This package contains library source intended for building other packages which
use the "EncodedVideoChunkType" feature of the "%{crate}" crate.

%package     -n %{name}+EndingTypes-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EndingTypes-devel

This package contains library source intended for building other packages which
use the "EndingTypes" feature of the "%{crate}" crate.

%package     -n %{name}+ErrorCallback-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ErrorCallback-devel

This package contains library source intended for building other packages which
use the "ErrorCallback" feature of the "%{crate}" crate.

%package     -n %{name}+ErrorEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ErrorEvent-devel

This package contains library source intended for building other packages which
use the "ErrorEvent" feature of the "%{crate}" crate.

%package     -n %{name}+ErrorEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ErrorEventInit-devel

This package contains library source intended for building other packages which
use the "ErrorEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+Event-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Event-devel

This package contains library source intended for building other packages which
use the "Event" feature of the "%{crate}" crate.

%package     -n %{name}+EventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EventInit-devel

This package contains library source intended for building other packages which
use the "EventInit" feature of the "%{crate}" crate.

%package     -n %{name}+EventListener-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EventListener-devel

This package contains library source intended for building other packages which
use the "EventListener" feature of the "%{crate}" crate.

%package     -n %{name}+EventListenerOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EventListenerOptions-devel

This package contains library source intended for building other packages which
use the "EventListenerOptions" feature of the "%{crate}" crate.

%package     -n %{name}+EventModifierInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EventModifierInit-devel

This package contains library source intended for building other packages which
use the "EventModifierInit" feature of the "%{crate}" crate.

%package     -n %{name}+EventSource-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EventSource-devel

This package contains library source intended for building other packages which
use the "EventSource" feature of the "%{crate}" crate.

%package     -n %{name}+EventSourceInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EventSourceInit-devel

This package contains library source intended for building other packages which
use the "EventSourceInit" feature of the "%{crate}" crate.

%package     -n %{name}+EventTarget-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+EventTarget-devel

This package contains library source intended for building other packages which
use the "EventTarget" feature of the "%{crate}" crate.

%package     -n %{name}+Exception-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Exception-devel

This package contains library source intended for building other packages which
use the "Exception" feature of the "%{crate}" crate.

%package     -n %{name}+ExtBlendMinmax-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtBlendMinmax-devel

This package contains library source intended for building other packages which
use the "ExtBlendMinmax" feature of the "%{crate}" crate.

%package     -n %{name}+ExtColorBufferFloat-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtColorBufferFloat-devel

This package contains library source intended for building other packages which
use the "ExtColorBufferFloat" feature of the "%{crate}" crate.

%package     -n %{name}+ExtColorBufferHalfFloat-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtColorBufferHalfFloat-devel

This package contains library source intended for building other packages which
use the "ExtColorBufferHalfFloat" feature of the "%{crate}" crate.

%package     -n %{name}+ExtDisjointTimerQuery-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtDisjointTimerQuery-devel

This package contains library source intended for building other packages which
use the "ExtDisjointTimerQuery" feature of the "%{crate}" crate.

%package     -n %{name}+ExtFragDepth-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtFragDepth-devel

This package contains library source intended for building other packages which
use the "ExtFragDepth" feature of the "%{crate}" crate.

%package     -n %{name}+ExtSRgb-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtSRgb-devel

This package contains library source intended for building other packages which
use the "ExtSRgb" feature of the "%{crate}" crate.

%package     -n %{name}+ExtShaderTextureLod-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtShaderTextureLod-devel

This package contains library source intended for building other packages which
use the "ExtShaderTextureLod" feature of the "%{crate}" crate.

%package     -n %{name}+ExtTextureFilterAnisotropic-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtTextureFilterAnisotropic-devel

This package contains library source intended for building other packages which
use the "ExtTextureFilterAnisotropic" feature of the "%{crate}" crate.

%package     -n %{name}+ExtTextureNorm16-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtTextureNorm16-devel

This package contains library source intended for building other packages which
use the "ExtTextureNorm16" feature of the "%{crate}" crate.

%package     -n %{name}+ExtendableCookieChangeEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtendableCookieChangeEvent-devel

This package contains library source intended for building other packages which
use the "ExtendableCookieChangeEvent" feature of the "%{crate}" crate.

%package     -n %{name}+ExtendableCookieChangeEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtendableCookieChangeEventInit-devel

This package contains library source intended for building other packages which
use the "ExtendableCookieChangeEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+ExtendableEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtendableEvent-devel

This package contains library source intended for building other packages which
use the "ExtendableEvent" feature of the "%{crate}" crate.

%package     -n %{name}+ExtendableEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtendableEventInit-devel

This package contains library source intended for building other packages which
use the "ExtendableEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+ExtendableMessageEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtendableMessageEvent-devel

This package contains library source intended for building other packages which
use the "ExtendableMessageEvent" feature of the "%{crate}" crate.

%package     -n %{name}+ExtendableMessageEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ExtendableMessageEventInit-devel

This package contains library source intended for building other packages which
use the "ExtendableMessageEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+External-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+External-devel

This package contains library source intended for building other packages which
use the "External" feature of the "%{crate}" crate.

%package     -n %{name}+FakePluginMimeEntry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FakePluginMimeEntry-devel

This package contains library source intended for building other packages which
use the "FakePluginMimeEntry" feature of the "%{crate}" crate.

%package     -n %{name}+FakePluginTagInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FakePluginTagInit-devel

This package contains library source intended for building other packages which
use the "FakePluginTagInit" feature of the "%{crate}" crate.

%package     -n %{name}+FetchEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FetchEvent-devel

This package contains library source intended for building other packages which
use the "FetchEvent" feature of the "%{crate}" crate.

%package     -n %{name}+FetchEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FetchEventInit-devel

This package contains library source intended for building other packages which
use the "FetchEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+FetchObserver-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FetchObserver-devel

This package contains library source intended for building other packages which
use the "FetchObserver" feature of the "%{crate}" crate.

%package     -n %{name}+FetchReadableStreamReadDataArray-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FetchReadableStreamReadDataArray-devel

This package contains library source intended for building other packages which
use the "FetchReadableStreamReadDataArray" feature of the "%{crate}" crate.

%package     -n %{name}+FetchReadableStreamReadDataDone-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FetchReadableStreamReadDataDone-devel

This package contains library source intended for building other packages which
use the "FetchReadableStreamReadDataDone" feature of the "%{crate}" crate.

%package     -n %{name}+FetchState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FetchState-devel

This package contains library source intended for building other packages which
use the "FetchState" feature of the "%{crate}" crate.

%package     -n %{name}+File-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+File-devel

This package contains library source intended for building other packages which
use the "File" feature of the "%{crate}" crate.

%package     -n %{name}+FileCallback-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileCallback-devel

This package contains library source intended for building other packages which
use the "FileCallback" feature of the "%{crate}" crate.

%package     -n %{name}+FileList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileList-devel

This package contains library source intended for building other packages which
use the "FileList" feature of the "%{crate}" crate.

%package     -n %{name}+FilePickerAcceptType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FilePickerAcceptType-devel

This package contains library source intended for building other packages which
use the "FilePickerAcceptType" feature of the "%{crate}" crate.

%package     -n %{name}+FilePickerOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FilePickerOptions-devel

This package contains library source intended for building other packages which
use the "FilePickerOptions" feature of the "%{crate}" crate.

%package     -n %{name}+FilePropertyBag-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FilePropertyBag-devel

This package contains library source intended for building other packages which
use the "FilePropertyBag" feature of the "%{crate}" crate.

%package     -n %{name}+FileReader-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileReader-devel

This package contains library source intended for building other packages which
use the "FileReader" feature of the "%{crate}" crate.

%package     -n %{name}+FileReaderSync-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileReaderSync-devel

This package contains library source intended for building other packages which
use the "FileReaderSync" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystem-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystem-devel

This package contains library source intended for building other packages which
use the "FileSystem" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemCreateWritableOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemCreateWritableOptions-devel

This package contains library source intended for building other packages which
use the "FileSystemCreateWritableOptions" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemDirectoryEntry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemDirectoryEntry-devel

This package contains library source intended for building other packages which
use the "FileSystemDirectoryEntry" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemDirectoryHandle-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemDirectoryHandle-devel

This package contains library source intended for building other packages which
use the "FileSystemDirectoryHandle" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemDirectoryReader-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemDirectoryReader-devel

This package contains library source intended for building other packages which
use the "FileSystemDirectoryReader" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemEntriesCallback-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemEntriesCallback-devel

This package contains library source intended for building other packages which
use the "FileSystemEntriesCallback" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemEntry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemEntry-devel

This package contains library source intended for building other packages which
use the "FileSystemEntry" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemEntryCallback-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemEntryCallback-devel

This package contains library source intended for building other packages which
use the "FileSystemEntryCallback" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemFileEntry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemFileEntry-devel

This package contains library source intended for building other packages which
use the "FileSystemFileEntry" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemFileHandle-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemFileHandle-devel

This package contains library source intended for building other packages which
use the "FileSystemFileHandle" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemFlags-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemFlags-devel

This package contains library source intended for building other packages which
use the "FileSystemFlags" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemGetDirectoryOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemGetDirectoryOptions-devel

This package contains library source intended for building other packages which
use the "FileSystemGetDirectoryOptions" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemGetFileOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemGetFileOptions-devel

This package contains library source intended for building other packages which
use the "FileSystemGetFileOptions" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemHandle-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemHandle-devel

This package contains library source intended for building other packages which
use the "FileSystemHandle" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemHandleKind-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemHandleKind-devel

This package contains library source intended for building other packages which
use the "FileSystemHandleKind" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemHandlePermissionDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemHandlePermissionDescriptor-devel

This package contains library source intended for building other packages which
use the "FileSystemHandlePermissionDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemPermissionDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemPermissionDescriptor-devel

This package contains library source intended for building other packages which
use the "FileSystemPermissionDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemPermissionMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemPermissionMode-devel

This package contains library source intended for building other packages which
use the "FileSystemPermissionMode" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemReadWriteOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemReadWriteOptions-devel

This package contains library source intended for building other packages which
use the "FileSystemReadWriteOptions" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemRemoveOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemRemoveOptions-devel

This package contains library source intended for building other packages which
use the "FileSystemRemoveOptions" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemSyncAccessHandle-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemSyncAccessHandle-devel

This package contains library source intended for building other packages which
use the "FileSystemSyncAccessHandle" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemSyncAccessHandleMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemSyncAccessHandleMode-devel

This package contains library source intended for building other packages which
use the "FileSystemSyncAccessHandleMode" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemSyncAccessHandleOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemSyncAccessHandleOptions-devel

This package contains library source intended for building other packages which
use the "FileSystemSyncAccessHandleOptions" feature of the "%{crate}" crate.

%package     -n %{name}+FileSystemWritableFileStream-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FileSystemWritableFileStream-devel

This package contains library source intended for building other packages which
use the "FileSystemWritableFileStream" feature of the "%{crate}" crate.

%package     -n %{name}+FillLightMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FillLightMode-devel

This package contains library source intended for building other packages which
use the "FillLightMode" feature of the "%{crate}" crate.

%package     -n %{name}+FillMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FillMode-devel

This package contains library source intended for building other packages which
use the "FillMode" feature of the "%{crate}" crate.

%package     -n %{name}+FlashClassification-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FlashClassification-devel

This package contains library source intended for building other packages which
use the "FlashClassification" feature of the "%{crate}" crate.

%package     -n %{name}+FlowControlType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FlowControlType-devel

This package contains library source intended for building other packages which
use the "FlowControlType" feature of the "%{crate}" crate.

%package     -n %{name}+FocusEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FocusEvent-devel

This package contains library source intended for building other packages which
use the "FocusEvent" feature of the "%{crate}" crate.

%package     -n %{name}+FocusEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FocusEventInit-devel

This package contains library source intended for building other packages which
use the "FocusEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+FocusOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FocusOptions-devel

This package contains library source intended for building other packages which
use the "FocusOptions" feature of the "%{crate}" crate.

%package     -n %{name}+FontData-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FontData-devel

This package contains library source intended for building other packages which
use the "FontData" feature of the "%{crate}" crate.

%package     -n %{name}+FontFace-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FontFace-devel

This package contains library source intended for building other packages which
use the "FontFace" feature of the "%{crate}" crate.

%package     -n %{name}+FontFaceDescriptors-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FontFaceDescriptors-devel

This package contains library source intended for building other packages which
use the "FontFaceDescriptors" feature of the "%{crate}" crate.

%package     -n %{name}+FontFaceLoadStatus-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FontFaceLoadStatus-devel

This package contains library source intended for building other packages which
use the "FontFaceLoadStatus" feature of the "%{crate}" crate.

%package     -n %{name}+FontFaceSet-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FontFaceSet-devel

This package contains library source intended for building other packages which
use the "FontFaceSet" feature of the "%{crate}" crate.

%package     -n %{name}+FontFaceSetIterator-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FontFaceSetIterator-devel

This package contains library source intended for building other packages which
use the "FontFaceSetIterator" feature of the "%{crate}" crate.

%package     -n %{name}+FontFaceSetIteratorResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FontFaceSetIteratorResult-devel

This package contains library source intended for building other packages which
use the "FontFaceSetIteratorResult" feature of the "%{crate}" crate.

%package     -n %{name}+FontFaceSetLoadEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FontFaceSetLoadEvent-devel

This package contains library source intended for building other packages which
use the "FontFaceSetLoadEvent" feature of the "%{crate}" crate.

%package     -n %{name}+FontFaceSetLoadEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FontFaceSetLoadEventInit-devel

This package contains library source intended for building other packages which
use the "FontFaceSetLoadEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+FontFaceSetLoadStatus-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FontFaceSetLoadStatus-devel

This package contains library source intended for building other packages which
use the "FontFaceSetLoadStatus" feature of the "%{crate}" crate.

%package     -n %{name}+FormData-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FormData-devel

This package contains library source intended for building other packages which
use the "FormData" feature of the "%{crate}" crate.

%package     -n %{name}+FrameType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FrameType-devel

This package contains library source intended for building other packages which
use the "FrameType" feature of the "%{crate}" crate.

%package     -n %{name}+FuzzingFunctions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+FuzzingFunctions-devel

This package contains library source intended for building other packages which
use the "FuzzingFunctions" feature of the "%{crate}" crate.

%package     -n %{name}+GainNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GainNode-devel

This package contains library source intended for building other packages which
use the "GainNode" feature of the "%{crate}" crate.

%package     -n %{name}+GainOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GainOptions-devel

This package contains library source intended for building other packages which
use the "GainOptions" feature of the "%{crate}" crate.

%package     -n %{name}+Gamepad-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Gamepad-devel

This package contains library source intended for building other packages which
use the "Gamepad" feature of the "%{crate}" crate.

%package     -n %{name}+GamepadButton-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GamepadButton-devel

This package contains library source intended for building other packages which
use the "GamepadButton" feature of the "%{crate}" crate.

%package     -n %{name}+GamepadEffectParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GamepadEffectParameters-devel

This package contains library source intended for building other packages which
use the "GamepadEffectParameters" feature of the "%{crate}" crate.

%package     -n %{name}+GamepadEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GamepadEvent-devel

This package contains library source intended for building other packages which
use the "GamepadEvent" feature of the "%{crate}" crate.

%package     -n %{name}+GamepadEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GamepadEventInit-devel

This package contains library source intended for building other packages which
use the "GamepadEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+GamepadHand-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GamepadHand-devel

This package contains library source intended for building other packages which
use the "GamepadHand" feature of the "%{crate}" crate.

%package     -n %{name}+GamepadHapticActuator-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GamepadHapticActuator-devel

This package contains library source intended for building other packages which
use the "GamepadHapticActuator" feature of the "%{crate}" crate.

%package     -n %{name}+GamepadHapticActuatorType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GamepadHapticActuatorType-devel

This package contains library source intended for building other packages which
use the "GamepadHapticActuatorType" feature of the "%{crate}" crate.

%package     -n %{name}+GamepadHapticEffectType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GamepadHapticEffectType-devel

This package contains library source intended for building other packages which
use the "GamepadHapticEffectType" feature of the "%{crate}" crate.

%package     -n %{name}+GamepadHapticsResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GamepadHapticsResult-devel

This package contains library source intended for building other packages which
use the "GamepadHapticsResult" feature of the "%{crate}" crate.

%package     -n %{name}+GamepadMappingType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GamepadMappingType-devel

This package contains library source intended for building other packages which
use the "GamepadMappingType" feature of the "%{crate}" crate.

%package     -n %{name}+GamepadPose-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GamepadPose-devel

This package contains library source intended for building other packages which
use the "GamepadPose" feature of the "%{crate}" crate.

%package     -n %{name}+GamepadTouch-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GamepadTouch-devel

This package contains library source intended for building other packages which
use the "GamepadTouch" feature of the "%{crate}" crate.

%package     -n %{name}+Geolocation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Geolocation-devel

This package contains library source intended for building other packages which
use the "Geolocation" feature of the "%{crate}" crate.

%package     -n %{name}+GeolocationCoordinates-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GeolocationCoordinates-devel

This package contains library source intended for building other packages which
use the "GeolocationCoordinates" feature of the "%{crate}" crate.

%package     -n %{name}+GeolocationPosition-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GeolocationPosition-devel

This package contains library source intended for building other packages which
use the "GeolocationPosition" feature of the "%{crate}" crate.

%package     -n %{name}+GeolocationPositionError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GeolocationPositionError-devel

This package contains library source intended for building other packages which
use the "GeolocationPositionError" feature of the "%{crate}" crate.

%package     -n %{name}+GestureEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GestureEvent-devel

This package contains library source intended for building other packages which
use the "GestureEvent" feature of the "%{crate}" crate.

%package     -n %{name}+GetAnimationsOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GetAnimationsOptions-devel

This package contains library source intended for building other packages which
use the "GetAnimationsOptions" feature of the "%{crate}" crate.

%package     -n %{name}+GetRootNodeOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GetRootNodeOptions-devel

This package contains library source intended for building other packages which
use the "GetRootNodeOptions" feature of the "%{crate}" crate.

%package     -n %{name}+GetUserMediaRequest-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GetUserMediaRequest-devel

This package contains library source intended for building other packages which
use the "GetUserMediaRequest" feature of the "%{crate}" crate.

%package     -n %{name}+Gpu-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Gpu-devel

This package contains library source intended for building other packages which
use the "Gpu" feature of the "%{crate}" crate.

%package     -n %{name}+GpuAdapter-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuAdapter-devel

This package contains library source intended for building other packages which
use the "GpuAdapter" feature of the "%{crate}" crate.

%package     -n %{name}+GpuAdapterInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuAdapterInfo-devel

This package contains library source intended for building other packages which
use the "GpuAdapterInfo" feature of the "%{crate}" crate.

%package     -n %{name}+GpuAddressMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuAddressMode-devel

This package contains library source intended for building other packages which
use the "GpuAddressMode" feature of the "%{crate}" crate.

%package     -n %{name}+GpuAutoLayoutMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuAutoLayoutMode-devel

This package contains library source intended for building other packages which
use the "GpuAutoLayoutMode" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBindGroup-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBindGroup-devel

This package contains library source intended for building other packages which
use the "GpuBindGroup" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBindGroupDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBindGroupDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuBindGroupDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBindGroupEntry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBindGroupEntry-devel

This package contains library source intended for building other packages which
use the "GpuBindGroupEntry" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBindGroupLayout-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBindGroupLayout-devel

This package contains library source intended for building other packages which
use the "GpuBindGroupLayout" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBindGroupLayoutDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBindGroupLayoutDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuBindGroupLayoutDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBindGroupLayoutEntry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBindGroupLayoutEntry-devel

This package contains library source intended for building other packages which
use the "GpuBindGroupLayoutEntry" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBlendComponent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBlendComponent-devel

This package contains library source intended for building other packages which
use the "GpuBlendComponent" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBlendFactor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBlendFactor-devel

This package contains library source intended for building other packages which
use the "GpuBlendFactor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBlendOperation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBlendOperation-devel

This package contains library source intended for building other packages which
use the "GpuBlendOperation" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBlendState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBlendState-devel

This package contains library source intended for building other packages which
use the "GpuBlendState" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBuffer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBuffer-devel

This package contains library source intended for building other packages which
use the "GpuBuffer" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBufferBinding-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBufferBinding-devel

This package contains library source intended for building other packages which
use the "GpuBufferBinding" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBufferBindingLayout-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBufferBindingLayout-devel

This package contains library source intended for building other packages which
use the "GpuBufferBindingLayout" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBufferBindingType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBufferBindingType-devel

This package contains library source intended for building other packages which
use the "GpuBufferBindingType" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBufferDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBufferDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuBufferDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuBufferMapState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuBufferMapState-devel

This package contains library source intended for building other packages which
use the "GpuBufferMapState" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCanvasAlphaMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCanvasAlphaMode-devel

This package contains library source intended for building other packages which
use the "GpuCanvasAlphaMode" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCanvasConfiguration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCanvasConfiguration-devel

This package contains library source intended for building other packages which
use the "GpuCanvasConfiguration" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCanvasContext-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCanvasContext-devel

This package contains library source intended for building other packages which
use the "GpuCanvasContext" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCanvasToneMapping-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCanvasToneMapping-devel

This package contains library source intended for building other packages which
use the "GpuCanvasToneMapping" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCanvasToneMappingMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCanvasToneMappingMode-devel

This package contains library source intended for building other packages which
use the "GpuCanvasToneMappingMode" feature of the "%{crate}" crate.

%package     -n %{name}+GpuColorDict-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuColorDict-devel

This package contains library source intended for building other packages which
use the "GpuColorDict" feature of the "%{crate}" crate.

%package     -n %{name}+GpuColorTargetState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuColorTargetState-devel

This package contains library source intended for building other packages which
use the "GpuColorTargetState" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCommandBuffer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCommandBuffer-devel

This package contains library source intended for building other packages which
use the "GpuCommandBuffer" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCommandBufferDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCommandBufferDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuCommandBufferDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCommandEncoder-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCommandEncoder-devel

This package contains library source intended for building other packages which
use the "GpuCommandEncoder" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCommandEncoderDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCommandEncoderDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuCommandEncoderDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCompareFunction-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCompareFunction-devel

This package contains library source intended for building other packages which
use the "GpuCompareFunction" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCompilationInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCompilationInfo-devel

This package contains library source intended for building other packages which
use the "GpuCompilationInfo" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCompilationMessage-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCompilationMessage-devel

This package contains library source intended for building other packages which
use the "GpuCompilationMessage" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCompilationMessageType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCompilationMessageType-devel

This package contains library source intended for building other packages which
use the "GpuCompilationMessageType" feature of the "%{crate}" crate.

%package     -n %{name}+GpuComputePassDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuComputePassDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuComputePassDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuComputePassEncoder-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuComputePassEncoder-devel

This package contains library source intended for building other packages which
use the "GpuComputePassEncoder" feature of the "%{crate}" crate.

%package     -n %{name}+GpuComputePassTimestampWrites-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuComputePassTimestampWrites-devel

This package contains library source intended for building other packages which
use the "GpuComputePassTimestampWrites" feature of the "%{crate}" crate.

%package     -n %{name}+GpuComputePipeline-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuComputePipeline-devel

This package contains library source intended for building other packages which
use the "GpuComputePipeline" feature of the "%{crate}" crate.

%package     -n %{name}+GpuComputePipelineDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuComputePipelineDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuComputePipelineDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCopyExternalImageDestInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCopyExternalImageDestInfo-devel

This package contains library source intended for building other packages which
use the "GpuCopyExternalImageDestInfo" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCopyExternalImageSourceInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCopyExternalImageSourceInfo-devel

This package contains library source intended for building other packages which
use the "GpuCopyExternalImageSourceInfo" feature of the "%{crate}" crate.

%package     -n %{name}+GpuCullMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuCullMode-devel

This package contains library source intended for building other packages which
use the "GpuCullMode" feature of the "%{crate}" crate.

%package     -n %{name}+GpuDepthStencilState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuDepthStencilState-devel

This package contains library source intended for building other packages which
use the "GpuDepthStencilState" feature of the "%{crate}" crate.

%package     -n %{name}+GpuDevice-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuDevice-devel

This package contains library source intended for building other packages which
use the "GpuDevice" feature of the "%{crate}" crate.

%package     -n %{name}+GpuDeviceDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuDeviceDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuDeviceDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuDeviceLostInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuDeviceLostInfo-devel

This package contains library source intended for building other packages which
use the "GpuDeviceLostInfo" feature of the "%{crate}" crate.

%package     -n %{name}+GpuDeviceLostReason-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuDeviceLostReason-devel

This package contains library source intended for building other packages which
use the "GpuDeviceLostReason" feature of the "%{crate}" crate.

%package     -n %{name}+GpuError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuError-devel

This package contains library source intended for building other packages which
use the "GpuError" feature of the "%{crate}" crate.

%package     -n %{name}+GpuErrorFilter-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuErrorFilter-devel

This package contains library source intended for building other packages which
use the "GpuErrorFilter" feature of the "%{crate}" crate.

%package     -n %{name}+GpuExtent3dDict-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuExtent3dDict-devel

This package contains library source intended for building other packages which
use the "GpuExtent3dDict" feature of the "%{crate}" crate.

%package     -n %{name}+GpuExternalTexture-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuExternalTexture-devel

This package contains library source intended for building other packages which
use the "GpuExternalTexture" feature of the "%{crate}" crate.

%package     -n %{name}+GpuExternalTextureBindingLayout-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuExternalTextureBindingLayout-devel

This package contains library source intended for building other packages which
use the "GpuExternalTextureBindingLayout" feature of the "%{crate}" crate.

%package     -n %{name}+GpuExternalTextureDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuExternalTextureDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuExternalTextureDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuFeatureName-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuFeatureName-devel

This package contains library source intended for building other packages which
use the "GpuFeatureName" feature of the "%{crate}" crate.

%package     -n %{name}+GpuFilterMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuFilterMode-devel

This package contains library source intended for building other packages which
use the "GpuFilterMode" feature of the "%{crate}" crate.

%package     -n %{name}+GpuFragmentState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuFragmentState-devel

This package contains library source intended for building other packages which
use the "GpuFragmentState" feature of the "%{crate}" crate.

%package     -n %{name}+GpuFrontFace-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuFrontFace-devel

This package contains library source intended for building other packages which
use the "GpuFrontFace" feature of the "%{crate}" crate.

%package     -n %{name}+GpuIndexFormat-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuIndexFormat-devel

This package contains library source intended for building other packages which
use the "GpuIndexFormat" feature of the "%{crate}" crate.

%package     -n %{name}+GpuInternalError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuInternalError-devel

This package contains library source intended for building other packages which
use the "GpuInternalError" feature of the "%{crate}" crate.

%package     -n %{name}+GpuLoadOp-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuLoadOp-devel

This package contains library source intended for building other packages which
use the "GpuLoadOp" feature of the "%{crate}" crate.

%package     -n %{name}+GpuMipmapFilterMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuMipmapFilterMode-devel

This package contains library source intended for building other packages which
use the "GpuMipmapFilterMode" feature of the "%{crate}" crate.

%package     -n %{name}+GpuMultisampleState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuMultisampleState-devel

This package contains library source intended for building other packages which
use the "GpuMultisampleState" feature of the "%{crate}" crate.

%package     -n %{name}+GpuObjectDescriptorBase-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuObjectDescriptorBase-devel

This package contains library source intended for building other packages which
use the "GpuObjectDescriptorBase" feature of the "%{crate}" crate.

%package     -n %{name}+GpuOrigin2dDict-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuOrigin2dDict-devel

This package contains library source intended for building other packages which
use the "GpuOrigin2dDict" feature of the "%{crate}" crate.

%package     -n %{name}+GpuOrigin3dDict-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuOrigin3dDict-devel

This package contains library source intended for building other packages which
use the "GpuOrigin3dDict" feature of the "%{crate}" crate.

%package     -n %{name}+GpuOutOfMemoryError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuOutOfMemoryError-devel

This package contains library source intended for building other packages which
use the "GpuOutOfMemoryError" feature of the "%{crate}" crate.

%package     -n %{name}+GpuPipelineDescriptorBase-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuPipelineDescriptorBase-devel

This package contains library source intended for building other packages which
use the "GpuPipelineDescriptorBase" feature of the "%{crate}" crate.

%package     -n %{name}+GpuPipelineError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuPipelineError-devel

This package contains library source intended for building other packages which
use the "GpuPipelineError" feature of the "%{crate}" crate.

%package     -n %{name}+GpuPipelineErrorInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuPipelineErrorInit-devel

This package contains library source intended for building other packages which
use the "GpuPipelineErrorInit" feature of the "%{crate}" crate.

%package     -n %{name}+GpuPipelineErrorReason-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuPipelineErrorReason-devel

This package contains library source intended for building other packages which
use the "GpuPipelineErrorReason" feature of the "%{crate}" crate.

%package     -n %{name}+GpuPipelineLayout-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuPipelineLayout-devel

This package contains library source intended for building other packages which
use the "GpuPipelineLayout" feature of the "%{crate}" crate.

%package     -n %{name}+GpuPipelineLayoutDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuPipelineLayoutDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuPipelineLayoutDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuPowerPreference-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuPowerPreference-devel

This package contains library source intended for building other packages which
use the "GpuPowerPreference" feature of the "%{crate}" crate.

%package     -n %{name}+GpuPrimitiveState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuPrimitiveState-devel

This package contains library source intended for building other packages which
use the "GpuPrimitiveState" feature of the "%{crate}" crate.

%package     -n %{name}+GpuPrimitiveTopology-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuPrimitiveTopology-devel

This package contains library source intended for building other packages which
use the "GpuPrimitiveTopology" feature of the "%{crate}" crate.

%package     -n %{name}+GpuProgrammableStage-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuProgrammableStage-devel

This package contains library source intended for building other packages which
use the "GpuProgrammableStage" feature of the "%{crate}" crate.

%package     -n %{name}+GpuQuerySet-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuQuerySet-devel

This package contains library source intended for building other packages which
use the "GpuQuerySet" feature of the "%{crate}" crate.

%package     -n %{name}+GpuQuerySetDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuQuerySetDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuQuerySetDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuQueryType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuQueryType-devel

This package contains library source intended for building other packages which
use the "GpuQueryType" feature of the "%{crate}" crate.

%package     -n %{name}+GpuQueue-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuQueue-devel

This package contains library source intended for building other packages which
use the "GpuQueue" feature of the "%{crate}" crate.

%package     -n %{name}+GpuQueueDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuQueueDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuQueueDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuRenderBundle-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuRenderBundle-devel

This package contains library source intended for building other packages which
use the "GpuRenderBundle" feature of the "%{crate}" crate.

%package     -n %{name}+GpuRenderBundleDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuRenderBundleDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuRenderBundleDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuRenderBundleEncoder-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuRenderBundleEncoder-devel

This package contains library source intended for building other packages which
use the "GpuRenderBundleEncoder" feature of the "%{crate}" crate.

%package     -n %{name}+GpuRenderBundleEncoderDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuRenderBundleEncoderDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuRenderBundleEncoderDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuRenderPassColorAttachment-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuRenderPassColorAttachment-devel

This package contains library source intended for building other packages which
use the "GpuRenderPassColorAttachment" feature of the "%{crate}" crate.

%package     -n %{name}+GpuRenderPassDepthStencilAttachment-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuRenderPassDepthStencilAttachment-devel

This package contains library source intended for building other packages which
use the "GpuRenderPassDepthStencilAttachment" feature of the "%{crate}" crate.

%package     -n %{name}+GpuRenderPassDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuRenderPassDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuRenderPassDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuRenderPassEncoder-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuRenderPassEncoder-devel

This package contains library source intended for building other packages which
use the "GpuRenderPassEncoder" feature of the "%{crate}" crate.

%package     -n %{name}+GpuRenderPassLayout-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuRenderPassLayout-devel

This package contains library source intended for building other packages which
use the "GpuRenderPassLayout" feature of the "%{crate}" crate.

%package     -n %{name}+GpuRenderPassTimestampWrites-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuRenderPassTimestampWrites-devel

This package contains library source intended for building other packages which
use the "GpuRenderPassTimestampWrites" feature of the "%{crate}" crate.

%package     -n %{name}+GpuRenderPipeline-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuRenderPipeline-devel

This package contains library source intended for building other packages which
use the "GpuRenderPipeline" feature of the "%{crate}" crate.

%package     -n %{name}+GpuRenderPipelineDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuRenderPipelineDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuRenderPipelineDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuRequestAdapterOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuRequestAdapterOptions-devel

This package contains library source intended for building other packages which
use the "GpuRequestAdapterOptions" feature of the "%{crate}" crate.

%package     -n %{name}+GpuSampler-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuSampler-devel

This package contains library source intended for building other packages which
use the "GpuSampler" feature of the "%{crate}" crate.

%package     -n %{name}+GpuSamplerBindingLayout-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuSamplerBindingLayout-devel

This package contains library source intended for building other packages which
use the "GpuSamplerBindingLayout" feature of the "%{crate}" crate.

%package     -n %{name}+GpuSamplerBindingType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuSamplerBindingType-devel

This package contains library source intended for building other packages which
use the "GpuSamplerBindingType" feature of the "%{crate}" crate.

%package     -n %{name}+GpuSamplerDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuSamplerDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuSamplerDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuShaderModule-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuShaderModule-devel

This package contains library source intended for building other packages which
use the "GpuShaderModule" feature of the "%{crate}" crate.

%package     -n %{name}+GpuShaderModuleCompilationHint-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuShaderModuleCompilationHint-devel

This package contains library source intended for building other packages which
use the "GpuShaderModuleCompilationHint" feature of the "%{crate}" crate.

%package     -n %{name}+GpuShaderModuleDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuShaderModuleDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuShaderModuleDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuStencilFaceState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuStencilFaceState-devel

This package contains library source intended for building other packages which
use the "GpuStencilFaceState" feature of the "%{crate}" crate.

%package     -n %{name}+GpuStencilOperation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuStencilOperation-devel

This package contains library source intended for building other packages which
use the "GpuStencilOperation" feature of the "%{crate}" crate.

%package     -n %{name}+GpuStorageTextureAccess-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuStorageTextureAccess-devel

This package contains library source intended for building other packages which
use the "GpuStorageTextureAccess" feature of the "%{crate}" crate.

%package     -n %{name}+GpuStorageTextureBindingLayout-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuStorageTextureBindingLayout-devel

This package contains library source intended for building other packages which
use the "GpuStorageTextureBindingLayout" feature of the "%{crate}" crate.

%package     -n %{name}+GpuStoreOp-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuStoreOp-devel

This package contains library source intended for building other packages which
use the "GpuStoreOp" feature of the "%{crate}" crate.

%package     -n %{name}+GpuSupportedFeatures-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuSupportedFeatures-devel

This package contains library source intended for building other packages which
use the "GpuSupportedFeatures" feature of the "%{crate}" crate.

%package     -n %{name}+GpuSupportedLimits-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuSupportedLimits-devel

This package contains library source intended for building other packages which
use the "GpuSupportedLimits" feature of the "%{crate}" crate.

%package     -n %{name}+GpuTexelCopyBufferInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuTexelCopyBufferInfo-devel

This package contains library source intended for building other packages which
use the "GpuTexelCopyBufferInfo" feature of the "%{crate}" crate.

%package     -n %{name}+GpuTexelCopyBufferLayout-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuTexelCopyBufferLayout-devel

This package contains library source intended for building other packages which
use the "GpuTexelCopyBufferLayout" feature of the "%{crate}" crate.

%package     -n %{name}+GpuTexelCopyTextureInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuTexelCopyTextureInfo-devel

This package contains library source intended for building other packages which
use the "GpuTexelCopyTextureInfo" feature of the "%{crate}" crate.

%package     -n %{name}+GpuTexture-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuTexture-devel

This package contains library source intended for building other packages which
use the "GpuTexture" feature of the "%{crate}" crate.

%package     -n %{name}+GpuTextureAspect-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuTextureAspect-devel

This package contains library source intended for building other packages which
use the "GpuTextureAspect" feature of the "%{crate}" crate.

%package     -n %{name}+GpuTextureBindingLayout-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuTextureBindingLayout-devel

This package contains library source intended for building other packages which
use the "GpuTextureBindingLayout" feature of the "%{crate}" crate.

%package     -n %{name}+GpuTextureDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuTextureDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuTextureDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuTextureDimension-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuTextureDimension-devel

This package contains library source intended for building other packages which
use the "GpuTextureDimension" feature of the "%{crate}" crate.

%package     -n %{name}+GpuTextureFormat-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuTextureFormat-devel

This package contains library source intended for building other packages which
use the "GpuTextureFormat" feature of the "%{crate}" crate.

%package     -n %{name}+GpuTextureSampleType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuTextureSampleType-devel

This package contains library source intended for building other packages which
use the "GpuTextureSampleType" feature of the "%{crate}" crate.

%package     -n %{name}+GpuTextureView-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuTextureView-devel

This package contains library source intended for building other packages which
use the "GpuTextureView" feature of the "%{crate}" crate.

%package     -n %{name}+GpuTextureViewDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuTextureViewDescriptor-devel

This package contains library source intended for building other packages which
use the "GpuTextureViewDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+GpuTextureViewDimension-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuTextureViewDimension-devel

This package contains library source intended for building other packages which
use the "GpuTextureViewDimension" feature of the "%{crate}" crate.

%package     -n %{name}+GpuUncapturedErrorEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuUncapturedErrorEvent-devel

This package contains library source intended for building other packages which
use the "GpuUncapturedErrorEvent" feature of the "%{crate}" crate.

%package     -n %{name}+GpuUncapturedErrorEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuUncapturedErrorEventInit-devel

This package contains library source intended for building other packages which
use the "GpuUncapturedErrorEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+GpuValidationError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuValidationError-devel

This package contains library source intended for building other packages which
use the "GpuValidationError" feature of the "%{crate}" crate.

%package     -n %{name}+GpuVertexAttribute-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuVertexAttribute-devel

This package contains library source intended for building other packages which
use the "GpuVertexAttribute" feature of the "%{crate}" crate.

%package     -n %{name}+GpuVertexBufferLayout-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuVertexBufferLayout-devel

This package contains library source intended for building other packages which
use the "GpuVertexBufferLayout" feature of the "%{crate}" crate.

%package     -n %{name}+GpuVertexFormat-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuVertexFormat-devel

This package contains library source intended for building other packages which
use the "GpuVertexFormat" feature of the "%{crate}" crate.

%package     -n %{name}+GpuVertexState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuVertexState-devel

This package contains library source intended for building other packages which
use the "GpuVertexState" feature of the "%{crate}" crate.

%package     -n %{name}+GpuVertexStepMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GpuVertexStepMode-devel

This package contains library source intended for building other packages which
use the "GpuVertexStepMode" feature of the "%{crate}" crate.

%package     -n %{name}+GroupedHistoryEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+GroupedHistoryEventInit-devel

This package contains library source intended for building other packages which
use the "GroupedHistoryEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+HalfOpenInfoDict-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HalfOpenInfoDict-devel

This package contains library source intended for building other packages which
use the "HalfOpenInfoDict" feature of the "%{crate}" crate.

%package     -n %{name}+HardwareAcceleration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HardwareAcceleration-devel

This package contains library source intended for building other packages which
use the "HardwareAcceleration" feature of the "%{crate}" crate.

%package     -n %{name}+HashChangeEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HashChangeEvent-devel

This package contains library source intended for building other packages which
use the "HashChangeEvent" feature of the "%{crate}" crate.

%package     -n %{name}+HashChangeEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HashChangeEventInit-devel

This package contains library source intended for building other packages which
use the "HashChangeEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+Headers-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Headers-devel

This package contains library source intended for building other packages which
use the "Headers" feature of the "%{crate}" crate.

%package     -n %{name}+HeadersGuardEnum-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HeadersGuardEnum-devel

This package contains library source intended for building other packages which
use the "HeadersGuardEnum" feature of the "%{crate}" crate.

%package     -n %{name}+Hid-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Hid-devel

This package contains library source intended for building other packages which
use the "Hid" feature of the "%{crate}" crate.

%package     -n %{name}+HidCollectionInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HidCollectionInfo-devel

This package contains library source intended for building other packages which
use the "HidCollectionInfo" feature of the "%{crate}" crate.

%package     -n %{name}+HidConnectionEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HidConnectionEvent-devel

This package contains library source intended for building other packages which
use the "HidConnectionEvent" feature of the "%{crate}" crate.

%package     -n %{name}+HidConnectionEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HidConnectionEventInit-devel

This package contains library source intended for building other packages which
use the "HidConnectionEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+HidDevice-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HidDevice-devel

This package contains library source intended for building other packages which
use the "HidDevice" feature of the "%{crate}" crate.

%package     -n %{name}+HidDeviceFilter-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HidDeviceFilter-devel

This package contains library source intended for building other packages which
use the "HidDeviceFilter" feature of the "%{crate}" crate.

%package     -n %{name}+HidDeviceRequestOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HidDeviceRequestOptions-devel

This package contains library source intended for building other packages which
use the "HidDeviceRequestOptions" feature of the "%{crate}" crate.

%package     -n %{name}+HidInputReportEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HidInputReportEvent-devel

This package contains library source intended for building other packages which
use the "HidInputReportEvent" feature of the "%{crate}" crate.

%package     -n %{name}+HidInputReportEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HidInputReportEventInit-devel

This package contains library source intended for building other packages which
use the "HidInputReportEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+HidReportInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HidReportInfo-devel

This package contains library source intended for building other packages which
use the "HidReportInfo" feature of the "%{crate}" crate.

%package     -n %{name}+HidReportItem-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HidReportItem-devel

This package contains library source intended for building other packages which
use the "HidReportItem" feature of the "%{crate}" crate.

%package     -n %{name}+HidUnitSystem-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HidUnitSystem-devel

This package contains library source intended for building other packages which
use the "HidUnitSystem" feature of the "%{crate}" crate.

%package     -n %{name}+HiddenPluginEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HiddenPluginEventInit-devel

This package contains library source intended for building other packages which
use the "HiddenPluginEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+Highlight-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Highlight-devel

This package contains library source intended for building other packages which
use the "Highlight" feature of the "%{crate}" crate.

%package     -n %{name}+HighlightHitResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HighlightHitResult-devel

This package contains library source intended for building other packages which
use the "HighlightHitResult" feature of the "%{crate}" crate.

%package     -n %{name}+HighlightRegistry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HighlightRegistry-devel

This package contains library source intended for building other packages which
use the "HighlightRegistry" feature of the "%{crate}" crate.

%package     -n %{name}+HighlightType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HighlightType-devel

This package contains library source intended for building other packages which
use the "HighlightType" feature of the "%{crate}" crate.

%package     -n %{name}+HighlightsFromPointOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HighlightsFromPointOptions-devel

This package contains library source intended for building other packages which
use the "HighlightsFromPointOptions" feature of the "%{crate}" crate.

%package     -n %{name}+History-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+History-devel

This package contains library source intended for building other packages which
use the "History" feature of the "%{crate}" crate.

%package     -n %{name}+HitRegionOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HitRegionOptions-devel

This package contains library source intended for building other packages which
use the "HitRegionOptions" feature of the "%{crate}" crate.

%package     -n %{name}+HkdfParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HkdfParams-devel

This package contains library source intended for building other packages which
use the "HkdfParams" feature of the "%{crate}" crate.

%package     -n %{name}+HmacDerivedKeyParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HmacDerivedKeyParams-devel

This package contains library source intended for building other packages which
use the "HmacDerivedKeyParams" feature of the "%{crate}" crate.

%package     -n %{name}+HmacImportParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HmacImportParams-devel

This package contains library source intended for building other packages which
use the "HmacImportParams" feature of the "%{crate}" crate.

%package     -n %{name}+HmacKeyAlgorithm-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HmacKeyAlgorithm-devel

This package contains library source intended for building other packages which
use the "HmacKeyAlgorithm" feature of the "%{crate}" crate.

%package     -n %{name}+HmacKeyGenParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HmacKeyGenParams-devel

This package contains library source intended for building other packages which
use the "HmacKeyGenParams" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlAllCollection-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlAllCollection-devel

This package contains library source intended for building other packages which
use the "HtmlAllCollection" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlAnchorElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlAnchorElement-devel

This package contains library source intended for building other packages which
use the "HtmlAnchorElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlAreaElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlAreaElement-devel

This package contains library source intended for building other packages which
use the "HtmlAreaElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlAudioElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlAudioElement-devel

This package contains library source intended for building other packages which
use the "HtmlAudioElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlBaseElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlBaseElement-devel

This package contains library source intended for building other packages which
use the "HtmlBaseElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlBodyElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlBodyElement-devel

This package contains library source intended for building other packages which
use the "HtmlBodyElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlBrElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlBrElement-devel

This package contains library source intended for building other packages which
use the "HtmlBrElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlButtonElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlButtonElement-devel

This package contains library source intended for building other packages which
use the "HtmlButtonElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlCanvasElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlCanvasElement-devel

This package contains library source intended for building other packages which
use the "HtmlCanvasElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlCollection-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlCollection-devel

This package contains library source intended for building other packages which
use the "HtmlCollection" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlDListElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlDListElement-devel

This package contains library source intended for building other packages which
use the "HtmlDListElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlDataElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlDataElement-devel

This package contains library source intended for building other packages which
use the "HtmlDataElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlDataListElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlDataListElement-devel

This package contains library source intended for building other packages which
use the "HtmlDataListElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlDetailsElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlDetailsElement-devel

This package contains library source intended for building other packages which
use the "HtmlDetailsElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlDialogElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlDialogElement-devel

This package contains library source intended for building other packages which
use the "HtmlDialogElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlDirectoryElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlDirectoryElement-devel

This package contains library source intended for building other packages which
use the "HtmlDirectoryElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlDivElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlDivElement-devel

This package contains library source intended for building other packages which
use the "HtmlDivElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlDocument-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlDocument-devel

This package contains library source intended for building other packages which
use the "HtmlDocument" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlElement-devel

This package contains library source intended for building other packages which
use the "HtmlElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlEmbedElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlEmbedElement-devel

This package contains library source intended for building other packages which
use the "HtmlEmbedElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlFieldSetElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlFieldSetElement-devel

This package contains library source intended for building other packages which
use the "HtmlFieldSetElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlFontElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlFontElement-devel

This package contains library source intended for building other packages which
use the "HtmlFontElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlFormControlsCollection-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlFormControlsCollection-devel

This package contains library source intended for building other packages which
use the "HtmlFormControlsCollection" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlFormElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlFormElement-devel

This package contains library source intended for building other packages which
use the "HtmlFormElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlFrameElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlFrameElement-devel

This package contains library source intended for building other packages which
use the "HtmlFrameElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlFrameSetElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlFrameSetElement-devel

This package contains library source intended for building other packages which
use the "HtmlFrameSetElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlHeadElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlHeadElement-devel

This package contains library source intended for building other packages which
use the "HtmlHeadElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlHeadingElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlHeadingElement-devel

This package contains library source intended for building other packages which
use the "HtmlHeadingElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlHrElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlHrElement-devel

This package contains library source intended for building other packages which
use the "HtmlHrElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlHtmlElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlHtmlElement-devel

This package contains library source intended for building other packages which
use the "HtmlHtmlElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlIFrameElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlIFrameElement-devel

This package contains library source intended for building other packages which
use the "HtmlIFrameElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlImageElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlImageElement-devel

This package contains library source intended for building other packages which
use the "HtmlImageElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlInputElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlInputElement-devel

This package contains library source intended for building other packages which
use the "HtmlInputElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlLabelElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlLabelElement-devel

This package contains library source intended for building other packages which
use the "HtmlLabelElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlLegendElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlLegendElement-devel

This package contains library source intended for building other packages which
use the "HtmlLegendElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlLiElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlLiElement-devel

This package contains library source intended for building other packages which
use the "HtmlLiElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlLinkElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlLinkElement-devel

This package contains library source intended for building other packages which
use the "HtmlLinkElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlMapElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlMapElement-devel

This package contains library source intended for building other packages which
use the "HtmlMapElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlMediaElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlMediaElement-devel

This package contains library source intended for building other packages which
use the "HtmlMediaElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlMenuElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlMenuElement-devel

This package contains library source intended for building other packages which
use the "HtmlMenuElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlMenuItemElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlMenuItemElement-devel

This package contains library source intended for building other packages which
use the "HtmlMenuItemElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlMetaElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlMetaElement-devel

This package contains library source intended for building other packages which
use the "HtmlMetaElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlMeterElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlMeterElement-devel

This package contains library source intended for building other packages which
use the "HtmlMeterElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlModElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlModElement-devel

This package contains library source intended for building other packages which
use the "HtmlModElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlOListElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlOListElement-devel

This package contains library source intended for building other packages which
use the "HtmlOListElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlObjectElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlObjectElement-devel

This package contains library source intended for building other packages which
use the "HtmlObjectElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlOptGroupElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlOptGroupElement-devel

This package contains library source intended for building other packages which
use the "HtmlOptGroupElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlOptionElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlOptionElement-devel

This package contains library source intended for building other packages which
use the "HtmlOptionElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlOptionsCollection-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlOptionsCollection-devel

This package contains library source intended for building other packages which
use the "HtmlOptionsCollection" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlOutputElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlOutputElement-devel

This package contains library source intended for building other packages which
use the "HtmlOutputElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlParagraphElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlParagraphElement-devel

This package contains library source intended for building other packages which
use the "HtmlParagraphElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlParamElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlParamElement-devel

This package contains library source intended for building other packages which
use the "HtmlParamElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlPictureElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlPictureElement-devel

This package contains library source intended for building other packages which
use the "HtmlPictureElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlPreElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlPreElement-devel

This package contains library source intended for building other packages which
use the "HtmlPreElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlProgressElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlProgressElement-devel

This package contains library source intended for building other packages which
use the "HtmlProgressElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlQuoteElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlQuoteElement-devel

This package contains library source intended for building other packages which
use the "HtmlQuoteElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlScriptElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlScriptElement-devel

This package contains library source intended for building other packages which
use the "HtmlScriptElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlSelectElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlSelectElement-devel

This package contains library source intended for building other packages which
use the "HtmlSelectElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlSlotElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlSlotElement-devel

This package contains library source intended for building other packages which
use the "HtmlSlotElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlSourceElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlSourceElement-devel

This package contains library source intended for building other packages which
use the "HtmlSourceElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlSpanElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlSpanElement-devel

This package contains library source intended for building other packages which
use the "HtmlSpanElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlStyleElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlStyleElement-devel

This package contains library source intended for building other packages which
use the "HtmlStyleElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlTableCaptionElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlTableCaptionElement-devel

This package contains library source intended for building other packages which
use the "HtmlTableCaptionElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlTableCellElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlTableCellElement-devel

This package contains library source intended for building other packages which
use the "HtmlTableCellElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlTableColElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlTableColElement-devel

This package contains library source intended for building other packages which
use the "HtmlTableColElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlTableElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlTableElement-devel

This package contains library source intended for building other packages which
use the "HtmlTableElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlTableRowElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlTableRowElement-devel

This package contains library source intended for building other packages which
use the "HtmlTableRowElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlTableSectionElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlTableSectionElement-devel

This package contains library source intended for building other packages which
use the "HtmlTableSectionElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlTemplateElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlTemplateElement-devel

This package contains library source intended for building other packages which
use the "HtmlTemplateElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlTextAreaElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlTextAreaElement-devel

This package contains library source intended for building other packages which
use the "HtmlTextAreaElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlTimeElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlTimeElement-devel

This package contains library source intended for building other packages which
use the "HtmlTimeElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlTitleElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlTitleElement-devel

This package contains library source intended for building other packages which
use the "HtmlTitleElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlTrackElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlTrackElement-devel

This package contains library source intended for building other packages which
use the "HtmlTrackElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlUListElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlUListElement-devel

This package contains library source intended for building other packages which
use the "HtmlUListElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlUnknownElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlUnknownElement-devel

This package contains library source intended for building other packages which
use the "HtmlUnknownElement" feature of the "%{crate}" crate.

%package     -n %{name}+HtmlVideoElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HtmlVideoElement-devel

This package contains library source intended for building other packages which
use the "HtmlVideoElement" feature of the "%{crate}" crate.

%package     -n %{name}+HttpConnDict-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HttpConnDict-devel

This package contains library source intended for building other packages which
use the "HttpConnDict" feature of the "%{crate}" crate.

%package     -n %{name}+HttpConnInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HttpConnInfo-devel

This package contains library source intended for building other packages which
use the "HttpConnInfo" feature of the "%{crate}" crate.

%package     -n %{name}+HttpConnectionElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+HttpConnectionElement-devel

This package contains library source intended for building other packages which
use the "HttpConnectionElement" feature of the "%{crate}" crate.

%package     -n %{name}+IdbCursor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbCursor-devel

This package contains library source intended for building other packages which
use the "IdbCursor" feature of the "%{crate}" crate.

%package     -n %{name}+IdbCursorDirection-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbCursorDirection-devel

This package contains library source intended for building other packages which
use the "IdbCursorDirection" feature of the "%{crate}" crate.

%package     -n %{name}+IdbCursorWithValue-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbCursorWithValue-devel

This package contains library source intended for building other packages which
use the "IdbCursorWithValue" feature of the "%{crate}" crate.

%package     -n %{name}+IdbDatabase-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbDatabase-devel

This package contains library source intended for building other packages which
use the "IdbDatabase" feature of the "%{crate}" crate.

%package     -n %{name}+IdbFactory-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbFactory-devel

This package contains library source intended for building other packages which
use the "IdbFactory" feature of the "%{crate}" crate.

%package     -n %{name}+IdbFileHandle-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbFileHandle-devel

This package contains library source intended for building other packages which
use the "IdbFileHandle" feature of the "%{crate}" crate.

%package     -n %{name}+IdbFileMetadataParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbFileMetadataParameters-devel

This package contains library source intended for building other packages which
use the "IdbFileMetadataParameters" feature of the "%{crate}" crate.

%package     -n %{name}+IdbFileRequest-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbFileRequest-devel

This package contains library source intended for building other packages which
use the "IdbFileRequest" feature of the "%{crate}" crate.

%package     -n %{name}+IdbIndex-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbIndex-devel

This package contains library source intended for building other packages which
use the "IdbIndex" feature of the "%{crate}" crate.

%package     -n %{name}+IdbIndexParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbIndexParameters-devel

This package contains library source intended for building other packages which
use the "IdbIndexParameters" feature of the "%{crate}" crate.

%package     -n %{name}+IdbKeyRange-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbKeyRange-devel

This package contains library source intended for building other packages which
use the "IdbKeyRange" feature of the "%{crate}" crate.

%package     -n %{name}+IdbLocaleAwareKeyRange-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbLocaleAwareKeyRange-devel

This package contains library source intended for building other packages which
use the "IdbLocaleAwareKeyRange" feature of the "%{crate}" crate.

%package     -n %{name}+IdbMutableFile-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbMutableFile-devel

This package contains library source intended for building other packages which
use the "IdbMutableFile" feature of the "%{crate}" crate.

%package     -n %{name}+IdbObjectStore-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbObjectStore-devel

This package contains library source intended for building other packages which
use the "IdbObjectStore" feature of the "%{crate}" crate.

%package     -n %{name}+IdbObjectStoreParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbObjectStoreParameters-devel

This package contains library source intended for building other packages which
use the "IdbObjectStoreParameters" feature of the "%{crate}" crate.

%package     -n %{name}+IdbOpenDbOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbOpenDbOptions-devel

This package contains library source intended for building other packages which
use the "IdbOpenDbOptions" feature of the "%{crate}" crate.

%package     -n %{name}+IdbOpenDbRequest-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbOpenDbRequest-devel

This package contains library source intended for building other packages which
use the "IdbOpenDbRequest" feature of the "%{crate}" crate.

%package     -n %{name}+IdbRequest-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbRequest-devel

This package contains library source intended for building other packages which
use the "IdbRequest" feature of the "%{crate}" crate.

%package     -n %{name}+IdbRequestReadyState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbRequestReadyState-devel

This package contains library source intended for building other packages which
use the "IdbRequestReadyState" feature of the "%{crate}" crate.

%package     -n %{name}+IdbTransaction-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbTransaction-devel

This package contains library source intended for building other packages which
use the "IdbTransaction" feature of the "%{crate}" crate.

%package     -n %{name}+IdbTransactionDurability-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbTransactionDurability-devel

This package contains library source intended for building other packages which
use the "IdbTransactionDurability" feature of the "%{crate}" crate.

%package     -n %{name}+IdbTransactionMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbTransactionMode-devel

This package contains library source intended for building other packages which
use the "IdbTransactionMode" feature of the "%{crate}" crate.

%package     -n %{name}+IdbTransactionOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbTransactionOptions-devel

This package contains library source intended for building other packages which
use the "IdbTransactionOptions" feature of the "%{crate}" crate.

%package     -n %{name}+IdbVersionChangeEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbVersionChangeEvent-devel

This package contains library source intended for building other packages which
use the "IdbVersionChangeEvent" feature of the "%{crate}" crate.

%package     -n %{name}+IdbVersionChangeEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdbVersionChangeEventInit-devel

This package contains library source intended for building other packages which
use the "IdbVersionChangeEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+IdleDeadline-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdleDeadline-devel

This package contains library source intended for building other packages which
use the "IdleDeadline" feature of the "%{crate}" crate.

%package     -n %{name}+IdleRequestOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IdleRequestOptions-devel

This package contains library source intended for building other packages which
use the "IdleRequestOptions" feature of the "%{crate}" crate.

%package     -n %{name}+IirFilterNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IirFilterNode-devel

This package contains library source intended for building other packages which
use the "IirFilterNode" feature of the "%{crate}" crate.

%package     -n %{name}+IirFilterOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IirFilterOptions-devel

This package contains library source intended for building other packages which
use the "IirFilterOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ImageBitmap-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageBitmap-devel

This package contains library source intended for building other packages which
use the "ImageBitmap" feature of the "%{crate}" crate.

%package     -n %{name}+ImageBitmapOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageBitmapOptions-devel

This package contains library source intended for building other packages which
use the "ImageBitmapOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ImageBitmapRenderingContext-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageBitmapRenderingContext-devel

This package contains library source intended for building other packages which
use the "ImageBitmapRenderingContext" feature of the "%{crate}" crate.

%package     -n %{name}+ImageCapture-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageCapture-devel

This package contains library source intended for building other packages which
use the "ImageCapture" feature of the "%{crate}" crate.

%package     -n %{name}+ImageCaptureError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageCaptureError-devel

This package contains library source intended for building other packages which
use the "ImageCaptureError" feature of the "%{crate}" crate.

%package     -n %{name}+ImageCaptureErrorEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageCaptureErrorEvent-devel

This package contains library source intended for building other packages which
use the "ImageCaptureErrorEvent" feature of the "%{crate}" crate.

%package     -n %{name}+ImageCaptureErrorEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageCaptureErrorEventInit-devel

This package contains library source intended for building other packages which
use the "ImageCaptureErrorEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+ImageData-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageData-devel

This package contains library source intended for building other packages which
use the "ImageData" feature of the "%{crate}" crate.

%package     -n %{name}+ImageDecodeOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageDecodeOptions-devel

This package contains library source intended for building other packages which
use the "ImageDecodeOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ImageDecodeResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageDecodeResult-devel

This package contains library source intended for building other packages which
use the "ImageDecodeResult" feature of the "%{crate}" crate.

%package     -n %{name}+ImageDecoder-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageDecoder-devel

This package contains library source intended for building other packages which
use the "ImageDecoder" feature of the "%{crate}" crate.

%package     -n %{name}+ImageDecoderInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageDecoderInit-devel

This package contains library source intended for building other packages which
use the "ImageDecoderInit" feature of the "%{crate}" crate.

%package     -n %{name}+ImageEncodeOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageEncodeOptions-devel

This package contains library source intended for building other packages which
use the "ImageEncodeOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ImageOrientation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageOrientation-devel

This package contains library source intended for building other packages which
use the "ImageOrientation" feature of the "%{crate}" crate.

%package     -n %{name}+ImageTrack-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageTrack-devel

This package contains library source intended for building other packages which
use the "ImageTrack" feature of the "%{crate}" crate.

%package     -n %{name}+ImageTrackList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ImageTrackList-devel

This package contains library source intended for building other packages which
use the "ImageTrackList" feature of the "%{crate}" crate.

%package     -n %{name}+InputDeviceInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+InputDeviceInfo-devel

This package contains library source intended for building other packages which
use the "InputDeviceInfo" feature of the "%{crate}" crate.

%package     -n %{name}+InputEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+InputEvent-devel

This package contains library source intended for building other packages which
use the "InputEvent" feature of the "%{crate}" crate.

%package     -n %{name}+InputEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+InputEventInit-devel

This package contains library source intended for building other packages which
use the "InputEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+IntersectionObserver-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IntersectionObserver-devel

This package contains library source intended for building other packages which
use the "IntersectionObserver" feature of the "%{crate}" crate.

%package     -n %{name}+IntersectionObserverEntry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IntersectionObserverEntry-devel

This package contains library source intended for building other packages which
use the "IntersectionObserverEntry" feature of the "%{crate}" crate.

%package     -n %{name}+IntersectionObserverEntryInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IntersectionObserverEntryInit-devel

This package contains library source intended for building other packages which
use the "IntersectionObserverEntryInit" feature of the "%{crate}" crate.

%package     -n %{name}+IntersectionObserverInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IntersectionObserverInit-devel

This package contains library source intended for building other packages which
use the "IntersectionObserverInit" feature of the "%{crate}" crate.

%package     -n %{name}+IntlUtils-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IntlUtils-devel

This package contains library source intended for building other packages which
use the "IntlUtils" feature of the "%{crate}" crate.

%package     -n %{name}+IsInputPendingOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IsInputPendingOptions-devel

This package contains library source intended for building other packages which
use the "IsInputPendingOptions" feature of the "%{crate}" crate.

%package     -n %{name}+IterableKeyAndValueResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IterableKeyAndValueResult-devel

This package contains library source intended for building other packages which
use the "IterableKeyAndValueResult" feature of the "%{crate}" crate.

%package     -n %{name}+IterableKeyOrValueResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IterableKeyOrValueResult-devel

This package contains library source intended for building other packages which
use the "IterableKeyOrValueResult" feature of the "%{crate}" crate.

%package     -n %{name}+IterationCompositeOperation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+IterationCompositeOperation-devel

This package contains library source intended for building other packages which
use the "IterationCompositeOperation" feature of the "%{crate}" crate.

%package     -n %{name}+JsonWebKey-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+JsonWebKey-devel

This package contains library source intended for building other packages which
use the "JsonWebKey" feature of the "%{crate}" crate.

%package     -n %{name}+KeyAlgorithm-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+KeyAlgorithm-devel

This package contains library source intended for building other packages which
use the "KeyAlgorithm" feature of the "%{crate}" crate.

%package     -n %{name}+KeyEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+KeyEvent-devel

This package contains library source intended for building other packages which
use the "KeyEvent" feature of the "%{crate}" crate.

%package     -n %{name}+KeyFrameRequestEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+KeyFrameRequestEvent-devel

This package contains library source intended for building other packages which
use the "KeyFrameRequestEvent" feature of the "%{crate}" crate.

%package     -n %{name}+KeyIdsInitData-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+KeyIdsInitData-devel

This package contains library source intended for building other packages which
use the "KeyIdsInitData" feature of the "%{crate}" crate.

%package     -n %{name}+KeyboardEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+KeyboardEvent-devel

This package contains library source intended for building other packages which
use the "KeyboardEvent" feature of the "%{crate}" crate.

%package     -n %{name}+KeyboardEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+KeyboardEventInit-devel

This package contains library source intended for building other packages which
use the "KeyboardEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+KeyframeAnimationOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+KeyframeAnimationOptions-devel

This package contains library source intended for building other packages which
use the "KeyframeAnimationOptions" feature of the "%{crate}" crate.

%package     -n %{name}+KeyframeEffect-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+KeyframeEffect-devel

This package contains library source intended for building other packages which
use the "KeyframeEffect" feature of the "%{crate}" crate.

%package     -n %{name}+KeyframeEffectOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+KeyframeEffectOptions-devel

This package contains library source intended for building other packages which
use the "KeyframeEffectOptions" feature of the "%{crate}" crate.

%package     -n %{name}+L10nElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+L10nElement-devel

This package contains library source intended for building other packages which
use the "L10nElement" feature of the "%{crate}" crate.

%package     -n %{name}+L10nValue-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+L10nValue-devel

This package contains library source intended for building other packages which
use the "L10nValue" feature of the "%{crate}" crate.

%package     -n %{name}+LargeBlobSupport-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+LargeBlobSupport-devel

This package contains library source intended for building other packages which
use the "LargeBlobSupport" feature of the "%{crate}" crate.

%package     -n %{name}+LatencyMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+LatencyMode-devel

This package contains library source intended for building other packages which
use the "LatencyMode" feature of the "%{crate}" crate.

%package     -n %{name}+LifecycleCallbacks-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+LifecycleCallbacks-devel

This package contains library source intended for building other packages which
use the "LifecycleCallbacks" feature of the "%{crate}" crate.

%package     -n %{name}+LineAlignSetting-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+LineAlignSetting-devel

This package contains library source intended for building other packages which
use the "LineAlignSetting" feature of the "%{crate}" crate.

%package     -n %{name}+ListBoxObject-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ListBoxObject-devel

This package contains library source intended for building other packages which
use the "ListBoxObject" feature of the "%{crate}" crate.

%package     -n %{name}+LocalMediaStream-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+LocalMediaStream-devel

This package contains library source intended for building other packages which
use the "LocalMediaStream" feature of the "%{crate}" crate.

%package     -n %{name}+LocaleInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+LocaleInfo-devel

This package contains library source intended for building other packages which
use the "LocaleInfo" feature of the "%{crate}" crate.

%package     -n %{name}+Location-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Location-devel

This package contains library source intended for building other packages which
use the "Location" feature of the "%{crate}" crate.

%package     -n %{name}+Lock-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Lock-devel

This package contains library source intended for building other packages which
use the "Lock" feature of the "%{crate}" crate.

%package     -n %{name}+LockInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+LockInfo-devel

This package contains library source intended for building other packages which
use the "LockInfo" feature of the "%{crate}" crate.

%package     -n %{name}+LockManager-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+LockManager-devel

This package contains library source intended for building other packages which
use the "LockManager" feature of the "%{crate}" crate.

%package     -n %{name}+LockManagerSnapshot-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+LockManagerSnapshot-devel

This package contains library source intended for building other packages which
use the "LockManagerSnapshot" feature of the "%{crate}" crate.

%package     -n %{name}+LockMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+LockMode-devel

This package contains library source intended for building other packages which
use the "LockMode" feature of the "%{crate}" crate.

%package     -n %{name}+LockOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+LockOptions-devel

This package contains library source intended for building other packages which
use the "LockOptions" feature of the "%{crate}" crate.

%package     -n %{name}+MathMlElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MathMlElement-devel

This package contains library source intended for building other packages which
use the "MathMlElement" feature of the "%{crate}" crate.

%package     -n %{name}+MediaCapabilities-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaCapabilities-devel

This package contains library source intended for building other packages which
use the "MediaCapabilities" feature of the "%{crate}" crate.

%package     -n %{name}+MediaCapabilitiesInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaCapabilitiesInfo-devel

This package contains library source intended for building other packages which
use the "MediaCapabilitiesInfo" feature of the "%{crate}" crate.

%package     -n %{name}+MediaConfiguration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaConfiguration-devel

This package contains library source intended for building other packages which
use the "MediaConfiguration" feature of the "%{crate}" crate.

%package     -n %{name}+MediaDecodingConfiguration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaDecodingConfiguration-devel

This package contains library source intended for building other packages which
use the "MediaDecodingConfiguration" feature of the "%{crate}" crate.

%package     -n %{name}+MediaDecodingType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaDecodingType-devel

This package contains library source intended for building other packages which
use the "MediaDecodingType" feature of the "%{crate}" crate.

%package     -n %{name}+MediaDeviceInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaDeviceInfo-devel

This package contains library source intended for building other packages which
use the "MediaDeviceInfo" feature of the "%{crate}" crate.

%package     -n %{name}+MediaDeviceKind-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaDeviceKind-devel

This package contains library source intended for building other packages which
use the "MediaDeviceKind" feature of the "%{crate}" crate.

%package     -n %{name}+MediaDevices-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaDevices-devel

This package contains library source intended for building other packages which
use the "MediaDevices" feature of the "%{crate}" crate.

%package     -n %{name}+MediaElementAudioSourceNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaElementAudioSourceNode-devel

This package contains library source intended for building other packages which
use the "MediaElementAudioSourceNode" feature of the "%{crate}" crate.

%package     -n %{name}+MediaElementAudioSourceOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaElementAudioSourceOptions-devel

This package contains library source intended for building other packages which
use the "MediaElementAudioSourceOptions" feature of the "%{crate}" crate.

%package     -n %{name}+MediaEncodingConfiguration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaEncodingConfiguration-devel

This package contains library source intended for building other packages which
use the "MediaEncodingConfiguration" feature of the "%{crate}" crate.

%package     -n %{name}+MediaEncodingType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaEncodingType-devel

This package contains library source intended for building other packages which
use the "MediaEncodingType" feature of the "%{crate}" crate.

%package     -n %{name}+MediaEncryptedEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaEncryptedEvent-devel

This package contains library source intended for building other packages which
use the "MediaEncryptedEvent" feature of the "%{crate}" crate.

%package     -n %{name}+MediaError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaError-devel

This package contains library source intended for building other packages which
use the "MediaError" feature of the "%{crate}" crate.

%package     -n %{name}+MediaImage-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaImage-devel

This package contains library source intended for building other packages which
use the "MediaImage" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeyError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeyError-devel

This package contains library source intended for building other packages which
use the "MediaKeyError" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeyMessageEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeyMessageEvent-devel

This package contains library source intended for building other packages which
use the "MediaKeyMessageEvent" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeyMessageEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeyMessageEventInit-devel

This package contains library source intended for building other packages which
use the "MediaKeyMessageEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeyMessageType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeyMessageType-devel

This package contains library source intended for building other packages which
use the "MediaKeyMessageType" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeyNeededEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeyNeededEventInit-devel

This package contains library source intended for building other packages which
use the "MediaKeyNeededEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeySession-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeySession-devel

This package contains library source intended for building other packages which
use the "MediaKeySession" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeySessionType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeySessionType-devel

This package contains library source intended for building other packages which
use the "MediaKeySessionType" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeyStatus-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeyStatus-devel

This package contains library source intended for building other packages which
use the "MediaKeyStatus" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeyStatusMap-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeyStatusMap-devel

This package contains library source intended for building other packages which
use the "MediaKeyStatusMap" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeySystemAccess-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeySystemAccess-devel

This package contains library source intended for building other packages which
use the "MediaKeySystemAccess" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeySystemConfiguration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeySystemConfiguration-devel

This package contains library source intended for building other packages which
use the "MediaKeySystemConfiguration" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeySystemMediaCapability-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeySystemMediaCapability-devel

This package contains library source intended for building other packages which
use the "MediaKeySystemMediaCapability" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeySystemStatus-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeySystemStatus-devel

This package contains library source intended for building other packages which
use the "MediaKeySystemStatus" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeys-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeys-devel

This package contains library source intended for building other packages which
use the "MediaKeys" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeysPolicy-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeysPolicy-devel

This package contains library source intended for building other packages which
use the "MediaKeysPolicy" feature of the "%{crate}" crate.

%package     -n %{name}+MediaKeysRequirement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaKeysRequirement-devel

This package contains library source intended for building other packages which
use the "MediaKeysRequirement" feature of the "%{crate}" crate.

%package     -n %{name}+MediaList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaList-devel

This package contains library source intended for building other packages which
use the "MediaList" feature of the "%{crate}" crate.

%package     -n %{name}+MediaMetadata-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaMetadata-devel

This package contains library source intended for building other packages which
use the "MediaMetadata" feature of the "%{crate}" crate.

%package     -n %{name}+MediaMetadataInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaMetadataInit-devel

This package contains library source intended for building other packages which
use the "MediaMetadataInit" feature of the "%{crate}" crate.

%package     -n %{name}+MediaPositionState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaPositionState-devel

This package contains library source intended for building other packages which
use the "MediaPositionState" feature of the "%{crate}" crate.

%package     -n %{name}+MediaQueryList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaQueryList-devel

This package contains library source intended for building other packages which
use the "MediaQueryList" feature of the "%{crate}" crate.

%package     -n %{name}+MediaQueryListEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaQueryListEvent-devel

This package contains library source intended for building other packages which
use the "MediaQueryListEvent" feature of the "%{crate}" crate.

%package     -n %{name}+MediaQueryListEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaQueryListEventInit-devel

This package contains library source intended for building other packages which
use the "MediaQueryListEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+MediaRecorder-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaRecorder-devel

This package contains library source intended for building other packages which
use the "MediaRecorder" feature of the "%{crate}" crate.

%package     -n %{name}+MediaRecorderErrorEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaRecorderErrorEvent-devel

This package contains library source intended for building other packages which
use the "MediaRecorderErrorEvent" feature of the "%{crate}" crate.

%package     -n %{name}+MediaRecorderErrorEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaRecorderErrorEventInit-devel

This package contains library source intended for building other packages which
use the "MediaRecorderErrorEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+MediaRecorderOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaRecorderOptions-devel

This package contains library source intended for building other packages which
use the "MediaRecorderOptions" feature of the "%{crate}" crate.

%package     -n %{name}+MediaSession-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaSession-devel

This package contains library source intended for building other packages which
use the "MediaSession" feature of the "%{crate}" crate.

%package     -n %{name}+MediaSessionAction-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaSessionAction-devel

This package contains library source intended for building other packages which
use the "MediaSessionAction" feature of the "%{crate}" crate.

%package     -n %{name}+MediaSessionActionDetails-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaSessionActionDetails-devel

This package contains library source intended for building other packages which
use the "MediaSessionActionDetails" feature of the "%{crate}" crate.

%package     -n %{name}+MediaSessionPlaybackState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaSessionPlaybackState-devel

This package contains library source intended for building other packages which
use the "MediaSessionPlaybackState" feature of the "%{crate}" crate.

%package     -n %{name}+MediaSettingsRange-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaSettingsRange-devel

This package contains library source intended for building other packages which
use the "MediaSettingsRange" feature of the "%{crate}" crate.

%package     -n %{name}+MediaSource-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaSource-devel

This package contains library source intended for building other packages which
use the "MediaSource" feature of the "%{crate}" crate.

%package     -n %{name}+MediaSourceEndOfStreamError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaSourceEndOfStreamError-devel

This package contains library source intended for building other packages which
use the "MediaSourceEndOfStreamError" feature of the "%{crate}" crate.

%package     -n %{name}+MediaSourceEnum-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaSourceEnum-devel

This package contains library source intended for building other packages which
use the "MediaSourceEnum" feature of the "%{crate}" crate.

%package     -n %{name}+MediaSourceReadyState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaSourceReadyState-devel

This package contains library source intended for building other packages which
use the "MediaSourceReadyState" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStream-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStream-devel

This package contains library source intended for building other packages which
use the "MediaStream" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamAudioDestinationNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamAudioDestinationNode-devel

This package contains library source intended for building other packages which
use the "MediaStreamAudioDestinationNode" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamAudioSourceNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamAudioSourceNode-devel

This package contains library source intended for building other packages which
use the "MediaStreamAudioSourceNode" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamAudioSourceOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamAudioSourceOptions-devel

This package contains library source intended for building other packages which
use the "MediaStreamAudioSourceOptions" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamConstraints-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamConstraints-devel

This package contains library source intended for building other packages which
use the "MediaStreamConstraints" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamError-devel

This package contains library source intended for building other packages which
use the "MediaStreamError" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamEvent-devel

This package contains library source intended for building other packages which
use the "MediaStreamEvent" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamEventInit-devel

This package contains library source intended for building other packages which
use the "MediaStreamEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamTrack-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamTrack-devel

This package contains library source intended for building other packages which
use the "MediaStreamTrack" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamTrackEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamTrackEvent-devel

This package contains library source intended for building other packages which
use the "MediaStreamTrackEvent" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamTrackEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamTrackEventInit-devel

This package contains library source intended for building other packages which
use the "MediaStreamTrackEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamTrackGenerator-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamTrackGenerator-devel

This package contains library source intended for building other packages which
use the "MediaStreamTrackGenerator" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamTrackGeneratorInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamTrackGeneratorInit-devel

This package contains library source intended for building other packages which
use the "MediaStreamTrackGeneratorInit" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamTrackProcessor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamTrackProcessor-devel

This package contains library source intended for building other packages which
use the "MediaStreamTrackProcessor" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamTrackProcessorInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamTrackProcessorInit-devel

This package contains library source intended for building other packages which
use the "MediaStreamTrackProcessorInit" feature of the "%{crate}" crate.

%package     -n %{name}+MediaStreamTrackState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaStreamTrackState-devel

This package contains library source intended for building other packages which
use the "MediaStreamTrackState" feature of the "%{crate}" crate.

%package     -n %{name}+MediaTrackCapabilities-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaTrackCapabilities-devel

This package contains library source intended for building other packages which
use the "MediaTrackCapabilities" feature of the "%{crate}" crate.

%package     -n %{name}+MediaTrackConstraintSet-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaTrackConstraintSet-devel

This package contains library source intended for building other packages which
use the "MediaTrackConstraintSet" feature of the "%{crate}" crate.

%package     -n %{name}+MediaTrackConstraints-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaTrackConstraints-devel

This package contains library source intended for building other packages which
use the "MediaTrackConstraints" feature of the "%{crate}" crate.

%package     -n %{name}+MediaTrackSettings-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaTrackSettings-devel

This package contains library source intended for building other packages which
use the "MediaTrackSettings" feature of the "%{crate}" crate.

%package     -n %{name}+MediaTrackSupportedConstraints-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MediaTrackSupportedConstraints-devel

This package contains library source intended for building other packages which
use the "MediaTrackSupportedConstraints" feature of the "%{crate}" crate.

%package     -n %{name}+MemoryAttribution-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MemoryAttribution-devel

This package contains library source intended for building other packages which
use the "MemoryAttribution" feature of the "%{crate}" crate.

%package     -n %{name}+MemoryAttributionContainer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MemoryAttributionContainer-devel

This package contains library source intended for building other packages which
use the "MemoryAttributionContainer" feature of the "%{crate}" crate.

%package     -n %{name}+MemoryBreakdownEntry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MemoryBreakdownEntry-devel

This package contains library source intended for building other packages which
use the "MemoryBreakdownEntry" feature of the "%{crate}" crate.

%package     -n %{name}+MemoryMeasurement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MemoryMeasurement-devel

This package contains library source intended for building other packages which
use the "MemoryMeasurement" feature of the "%{crate}" crate.

%package     -n %{name}+MessageChannel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MessageChannel-devel

This package contains library source intended for building other packages which
use the "MessageChannel" feature of the "%{crate}" crate.

%package     -n %{name}+MessageEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MessageEvent-devel

This package contains library source intended for building other packages which
use the "MessageEvent" feature of the "%{crate}" crate.

%package     -n %{name}+MessageEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MessageEventInit-devel

This package contains library source intended for building other packages which
use the "MessageEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+MessagePort-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MessagePort-devel

This package contains library source intended for building other packages which
use the "MessagePort" feature of the "%{crate}" crate.

%package     -n %{name}+MeteringMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MeteringMode-devel

This package contains library source intended for building other packages which
use the "MeteringMode" feature of the "%{crate}" crate.

%package     -n %{name}+MidiAccess-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MidiAccess-devel

This package contains library source intended for building other packages which
use the "MidiAccess" feature of the "%{crate}" crate.

%package     -n %{name}+MidiConnectionEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MidiConnectionEvent-devel

This package contains library source intended for building other packages which
use the "MidiConnectionEvent" feature of the "%{crate}" crate.

%package     -n %{name}+MidiConnectionEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MidiConnectionEventInit-devel

This package contains library source intended for building other packages which
use the "MidiConnectionEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+MidiInput-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MidiInput-devel

This package contains library source intended for building other packages which
use the "MidiInput" feature of the "%{crate}" crate.

%package     -n %{name}+MidiInputMap-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MidiInputMap-devel

This package contains library source intended for building other packages which
use the "MidiInputMap" feature of the "%{crate}" crate.

%package     -n %{name}+MidiMessageEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MidiMessageEvent-devel

This package contains library source intended for building other packages which
use the "MidiMessageEvent" feature of the "%{crate}" crate.

%package     -n %{name}+MidiMessageEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MidiMessageEventInit-devel

This package contains library source intended for building other packages which
use the "MidiMessageEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+MidiOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MidiOptions-devel

This package contains library source intended for building other packages which
use the "MidiOptions" feature of the "%{crate}" crate.

%package     -n %{name}+MidiOutput-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MidiOutput-devel

This package contains library source intended for building other packages which
use the "MidiOutput" feature of the "%{crate}" crate.

%package     -n %{name}+MidiOutputMap-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MidiOutputMap-devel

This package contains library source intended for building other packages which
use the "MidiOutputMap" feature of the "%{crate}" crate.

%package     -n %{name}+MidiPort-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MidiPort-devel

This package contains library source intended for building other packages which
use the "MidiPort" feature of the "%{crate}" crate.

%package     -n %{name}+MidiPortConnectionState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MidiPortConnectionState-devel

This package contains library source intended for building other packages which
use the "MidiPortConnectionState" feature of the "%{crate}" crate.

%package     -n %{name}+MidiPortDeviceState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MidiPortDeviceState-devel

This package contains library source intended for building other packages which
use the "MidiPortDeviceState" feature of the "%{crate}" crate.

%package     -n %{name}+MidiPortType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MidiPortType-devel

This package contains library source intended for building other packages which
use the "MidiPortType" feature of the "%{crate}" crate.

%package     -n %{name}+MimeType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MimeType-devel

This package contains library source intended for building other packages which
use the "MimeType" feature of the "%{crate}" crate.

%package     -n %{name}+MimeTypeArray-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MimeTypeArray-devel

This package contains library source intended for building other packages which
use the "MimeTypeArray" feature of the "%{crate}" crate.

%package     -n %{name}+MouseEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MouseEvent-devel

This package contains library source intended for building other packages which
use the "MouseEvent" feature of the "%{crate}" crate.

%package     -n %{name}+MouseEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MouseEventInit-devel

This package contains library source intended for building other packages which
use the "MouseEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+MouseScrollEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MouseScrollEvent-devel

This package contains library source intended for building other packages which
use the "MouseScrollEvent" feature of the "%{crate}" crate.

%package     -n %{name}+MozDebug-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MozDebug-devel

This package contains library source intended for building other packages which
use the "MozDebug" feature of the "%{crate}" crate.

%package     -n %{name}+MutationEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MutationEvent-devel

This package contains library source intended for building other packages which
use the "MutationEvent" feature of the "%{crate}" crate.

%package     -n %{name}+MutationObserver-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MutationObserver-devel

This package contains library source intended for building other packages which
use the "MutationObserver" feature of the "%{crate}" crate.

%package     -n %{name}+MutationObserverInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MutationObserverInit-devel

This package contains library source intended for building other packages which
use the "MutationObserverInit" feature of the "%{crate}" crate.

%package     -n %{name}+MutationObservingInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MutationObservingInfo-devel

This package contains library source intended for building other packages which
use the "MutationObservingInfo" feature of the "%{crate}" crate.

%package     -n %{name}+MutationRecord-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+MutationRecord-devel

This package contains library source intended for building other packages which
use the "MutationRecord" feature of the "%{crate}" crate.

%package     -n %{name}+NamedNodeMap-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NamedNodeMap-devel

This package contains library source intended for building other packages which
use the "NamedNodeMap" feature of the "%{crate}" crate.

%package     -n %{name}+NativeOsFileReadOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NativeOsFileReadOptions-devel

This package contains library source intended for building other packages which
use the "NativeOsFileReadOptions" feature of the "%{crate}" crate.

%package     -n %{name}+NativeOsFileWriteAtomicOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NativeOsFileWriteAtomicOptions-devel

This package contains library source intended for building other packages which
use the "NativeOsFileWriteAtomicOptions" feature of the "%{crate}" crate.

%package     -n %{name}+NavigationType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NavigationType-devel

This package contains library source intended for building other packages which
use the "NavigationType" feature of the "%{crate}" crate.

%package     -n %{name}+Navigator-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Navigator-devel

This package contains library source intended for building other packages which
use the "Navigator" feature of the "%{crate}" crate.

%package     -n %{name}+NavigatorAutomationInformation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NavigatorAutomationInformation-devel

This package contains library source intended for building other packages which
use the "NavigatorAutomationInformation" feature of the "%{crate}" crate.

%package     -n %{name}+NavigatorUaBrandVersion-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NavigatorUaBrandVersion-devel

This package contains library source intended for building other packages which
use the "NavigatorUaBrandVersion" feature of the "%{crate}" crate.

%package     -n %{name}+NavigatorUaData-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NavigatorUaData-devel

This package contains library source intended for building other packages which
use the "NavigatorUaData" feature of the "%{crate}" crate.

%package     -n %{name}+NetworkCommandOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NetworkCommandOptions-devel

This package contains library source intended for building other packages which
use the "NetworkCommandOptions" feature of the "%{crate}" crate.

%package     -n %{name}+NetworkInformation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NetworkInformation-devel

This package contains library source intended for building other packages which
use the "NetworkInformation" feature of the "%{crate}" crate.

%package     -n %{name}+NetworkResultOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NetworkResultOptions-devel

This package contains library source intended for building other packages which
use the "NetworkResultOptions" feature of the "%{crate}" crate.

%package     -n %{name}+Node-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Node-devel

This package contains library source intended for building other packages which
use the "Node" feature of the "%{crate}" crate.

%package     -n %{name}+NodeFilter-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NodeFilter-devel

This package contains library source intended for building other packages which
use the "NodeFilter" feature of the "%{crate}" crate.

%package     -n %{name}+NodeIterator-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NodeIterator-devel

This package contains library source intended for building other packages which
use the "NodeIterator" feature of the "%{crate}" crate.

%package     -n %{name}+NodeList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NodeList-devel

This package contains library source intended for building other packages which
use the "NodeList" feature of the "%{crate}" crate.

%package     -n %{name}+Notification-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Notification-devel

This package contains library source intended for building other packages which
use the "Notification" feature of the "%{crate}" crate.

%package     -n %{name}+NotificationAction-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NotificationAction-devel

This package contains library source intended for building other packages which
use the "NotificationAction" feature of the "%{crate}" crate.

%package     -n %{name}+NotificationDirection-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NotificationDirection-devel

This package contains library source intended for building other packages which
use the "NotificationDirection" feature of the "%{crate}" crate.

%package     -n %{name}+NotificationEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NotificationEvent-devel

This package contains library source intended for building other packages which
use the "NotificationEvent" feature of the "%{crate}" crate.

%package     -n %{name}+NotificationEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NotificationEventInit-devel

This package contains library source intended for building other packages which
use the "NotificationEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+NotificationOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NotificationOptions-devel

This package contains library source intended for building other packages which
use the "NotificationOptions" feature of the "%{crate}" crate.

%package     -n %{name}+NotificationPermission-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+NotificationPermission-devel

This package contains library source intended for building other packages which
use the "NotificationPermission" feature of the "%{crate}" crate.

%package     -n %{name}+ObserverCallback-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ObserverCallback-devel

This package contains library source intended for building other packages which
use the "ObserverCallback" feature of the "%{crate}" crate.

%package     -n %{name}+OesElementIndexUint-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OesElementIndexUint-devel

This package contains library source intended for building other packages which
use the "OesElementIndexUint" feature of the "%{crate}" crate.

%package     -n %{name}+OesStandardDerivatives-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OesStandardDerivatives-devel

This package contains library source intended for building other packages which
use the "OesStandardDerivatives" feature of the "%{crate}" crate.

%package     -n %{name}+OesTextureFloat-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OesTextureFloat-devel

This package contains library source intended for building other packages which
use the "OesTextureFloat" feature of the "%{crate}" crate.

%package     -n %{name}+OesTextureFloatLinear-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OesTextureFloatLinear-devel

This package contains library source intended for building other packages which
use the "OesTextureFloatLinear" feature of the "%{crate}" crate.

%package     -n %{name}+OesTextureHalfFloat-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OesTextureHalfFloat-devel

This package contains library source intended for building other packages which
use the "OesTextureHalfFloat" feature of the "%{crate}" crate.

%package     -n %{name}+OesTextureHalfFloatLinear-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OesTextureHalfFloatLinear-devel

This package contains library source intended for building other packages which
use the "OesTextureHalfFloatLinear" feature of the "%{crate}" crate.

%package     -n %{name}+OesVertexArrayObject-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OesVertexArrayObject-devel

This package contains library source intended for building other packages which
use the "OesVertexArrayObject" feature of the "%{crate}" crate.

%package     -n %{name}+OfflineAudioCompletionEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OfflineAudioCompletionEvent-devel

This package contains library source intended for building other packages which
use the "OfflineAudioCompletionEvent" feature of the "%{crate}" crate.

%package     -n %{name}+OfflineAudioCompletionEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OfflineAudioCompletionEventInit-devel

This package contains library source intended for building other packages which
use the "OfflineAudioCompletionEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+OfflineAudioContext-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OfflineAudioContext-devel

This package contains library source intended for building other packages which
use the "OfflineAudioContext" feature of the "%{crate}" crate.

%package     -n %{name}+OfflineAudioContextOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OfflineAudioContextOptions-devel

This package contains library source intended for building other packages which
use the "OfflineAudioContextOptions" feature of the "%{crate}" crate.

%package     -n %{name}+OfflineResourceList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OfflineResourceList-devel

This package contains library source intended for building other packages which
use the "OfflineResourceList" feature of the "%{crate}" crate.

%package     -n %{name}+OffscreenCanvas-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OffscreenCanvas-devel

This package contains library source intended for building other packages which
use the "OffscreenCanvas" feature of the "%{crate}" crate.

%package     -n %{name}+OffscreenCanvasRenderingContext2d-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OffscreenCanvasRenderingContext2d-devel

This package contains library source intended for building other packages which
use the "OffscreenCanvasRenderingContext2d" feature of the "%{crate}" crate.

%package     -n %{name}+OpenFilePickerOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OpenFilePickerOptions-devel

This package contains library source intended for building other packages which
use the "OpenFilePickerOptions" feature of the "%{crate}" crate.

%package     -n %{name}+OpenWindowEventDetail-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OpenWindowEventDetail-devel

This package contains library source intended for building other packages which
use the "OpenWindowEventDetail" feature of the "%{crate}" crate.

%package     -n %{name}+OptionalEffectTiming-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OptionalEffectTiming-devel

This package contains library source intended for building other packages which
use the "OptionalEffectTiming" feature of the "%{crate}" crate.

%package     -n %{name}+OrientationLockType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OrientationLockType-devel

This package contains library source intended for building other packages which
use the "OrientationLockType" feature of the "%{crate}" crate.

%package     -n %{name}+OrientationType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OrientationType-devel

This package contains library source intended for building other packages which
use the "OrientationType" feature of the "%{crate}" crate.

%package     -n %{name}+OscillatorNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OscillatorNode-devel

This package contains library source intended for building other packages which
use the "OscillatorNode" feature of the "%{crate}" crate.

%package     -n %{name}+OscillatorOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OscillatorOptions-devel

This package contains library source intended for building other packages which
use the "OscillatorOptions" feature of the "%{crate}" crate.

%package     -n %{name}+OscillatorType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OscillatorType-devel

This package contains library source intended for building other packages which
use the "OscillatorType" feature of the "%{crate}" crate.

%package     -n %{name}+OverSampleType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OverSampleType-devel

This package contains library source intended for building other packages which
use the "OverSampleType" feature of the "%{crate}" crate.

%package     -n %{name}+OvrMultiview2-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+OvrMultiview2-devel

This package contains library source intended for building other packages which
use the "OvrMultiview2" feature of the "%{crate}" crate.

%package     -n %{name}+PageTransitionEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PageTransitionEvent-devel

This package contains library source intended for building other packages which
use the "PageTransitionEvent" feature of the "%{crate}" crate.

%package     -n %{name}+PageTransitionEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PageTransitionEventInit-devel

This package contains library source intended for building other packages which
use the "PageTransitionEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+PaintRequest-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PaintRequest-devel

This package contains library source intended for building other packages which
use the "PaintRequest" feature of the "%{crate}" crate.

%package     -n %{name}+PaintRequestList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PaintRequestList-devel

This package contains library source intended for building other packages which
use the "PaintRequestList" feature of the "%{crate}" crate.

%package     -n %{name}+PaintWorkletGlobalScope-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PaintWorkletGlobalScope-devel

This package contains library source intended for building other packages which
use the "PaintWorkletGlobalScope" feature of the "%{crate}" crate.

%package     -n %{name}+PannerNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PannerNode-devel

This package contains library source intended for building other packages which
use the "PannerNode" feature of the "%{crate}" crate.

%package     -n %{name}+PannerOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PannerOptions-devel

This package contains library source intended for building other packages which
use the "PannerOptions" feature of the "%{crate}" crate.

%package     -n %{name}+PanningModelType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PanningModelType-devel

This package contains library source intended for building other packages which
use the "PanningModelType" feature of the "%{crate}" crate.

%package     -n %{name}+ParityType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ParityType-devel

This package contains library source intended for building other packages which
use the "ParityType" feature of the "%{crate}" crate.

%package     -n %{name}+Path2d-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Path2d-devel

This package contains library source intended for building other packages which
use the "Path2d" feature of the "%{crate}" crate.

%package     -n %{name}+PaymentAddress-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PaymentAddress-devel

This package contains library source intended for building other packages which
use the "PaymentAddress" feature of the "%{crate}" crate.

%package     -n %{name}+PaymentComplete-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PaymentComplete-devel

This package contains library source intended for building other packages which
use the "PaymentComplete" feature of the "%{crate}" crate.

%package     -n %{name}+PaymentMethodChangeEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PaymentMethodChangeEvent-devel

This package contains library source intended for building other packages which
use the "PaymentMethodChangeEvent" feature of the "%{crate}" crate.

%package     -n %{name}+PaymentMethodChangeEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PaymentMethodChangeEventInit-devel

This package contains library source intended for building other packages which
use the "PaymentMethodChangeEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+PaymentRequestUpdateEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PaymentRequestUpdateEvent-devel

This package contains library source intended for building other packages which
use the "PaymentRequestUpdateEvent" feature of the "%{crate}" crate.

%package     -n %{name}+PaymentRequestUpdateEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PaymentRequestUpdateEventInit-devel

This package contains library source intended for building other packages which
use the "PaymentRequestUpdateEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+PaymentResponse-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PaymentResponse-devel

This package contains library source intended for building other packages which
use the "PaymentResponse" feature of the "%{crate}" crate.

%package     -n %{name}+Pbkdf2Params-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Pbkdf2Params-devel

This package contains library source intended for building other packages which
use the "Pbkdf2Params" feature of the "%{crate}" crate.

%package     -n %{name}+PcImplIceConnectionState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PcImplIceConnectionState-devel

This package contains library source intended for building other packages which
use the "PcImplIceConnectionState" feature of the "%{crate}" crate.

%package     -n %{name}+PcImplIceGatheringState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PcImplIceGatheringState-devel

This package contains library source intended for building other packages which
use the "PcImplIceGatheringState" feature of the "%{crate}" crate.

%package     -n %{name}+PcImplSignalingState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PcImplSignalingState-devel

This package contains library source intended for building other packages which
use the "PcImplSignalingState" feature of the "%{crate}" crate.

%package     -n %{name}+PcObserverStateType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PcObserverStateType-devel

This package contains library source intended for building other packages which
use the "PcObserverStateType" feature of the "%{crate}" crate.

%package     -n %{name}+Performance-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Performance-devel

This package contains library source intended for building other packages which
use the "Performance" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceEntry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceEntry-devel

This package contains library source intended for building other packages which
use the "PerformanceEntry" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceEntryEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceEntryEventInit-devel

This package contains library source intended for building other packages which
use the "PerformanceEntryEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceEntryFilterOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceEntryFilterOptions-devel

This package contains library source intended for building other packages which
use the "PerformanceEntryFilterOptions" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceMark-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceMark-devel

This package contains library source intended for building other packages which
use the "PerformanceMark" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceMarkOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceMarkOptions-devel

This package contains library source intended for building other packages which
use the "PerformanceMarkOptions" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceMeasure-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceMeasure-devel

This package contains library source intended for building other packages which
use the "PerformanceMeasure" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceMeasureOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceMeasureOptions-devel

This package contains library source intended for building other packages which
use the "PerformanceMeasureOptions" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceNavigation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceNavigation-devel

This package contains library source intended for building other packages which
use the "PerformanceNavigation" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceNavigationTiming-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceNavigationTiming-devel

This package contains library source intended for building other packages which
use the "PerformanceNavigationTiming" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceObserver-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceObserver-devel

This package contains library source intended for building other packages which
use the "PerformanceObserver" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceObserverEntryList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceObserverEntryList-devel

This package contains library source intended for building other packages which
use the "PerformanceObserverEntryList" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceObserverInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceObserverInit-devel

This package contains library source intended for building other packages which
use the "PerformanceObserverInit" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceResourceTiming-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceResourceTiming-devel

This package contains library source intended for building other packages which
use the "PerformanceResourceTiming" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceServerTiming-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceServerTiming-devel

This package contains library source intended for building other packages which
use the "PerformanceServerTiming" feature of the "%{crate}" crate.

%package     -n %{name}+PerformanceTiming-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PerformanceTiming-devel

This package contains library source intended for building other packages which
use the "PerformanceTiming" feature of the "%{crate}" crate.

%package     -n %{name}+PeriodicWave-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PeriodicWave-devel

This package contains library source intended for building other packages which
use the "PeriodicWave" feature of the "%{crate}" crate.

%package     -n %{name}+PeriodicWaveConstraints-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PeriodicWaveConstraints-devel

This package contains library source intended for building other packages which
use the "PeriodicWaveConstraints" feature of the "%{crate}" crate.

%package     -n %{name}+PeriodicWaveOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PeriodicWaveOptions-devel

This package contains library source intended for building other packages which
use the "PeriodicWaveOptions" feature of the "%{crate}" crate.

%package     -n %{name}+PermissionDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PermissionDescriptor-devel

This package contains library source intended for building other packages which
use the "PermissionDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+PermissionName-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PermissionName-devel

This package contains library source intended for building other packages which
use the "PermissionName" feature of the "%{crate}" crate.

%package     -n %{name}+PermissionState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PermissionState-devel

This package contains library source intended for building other packages which
use the "PermissionState" feature of the "%{crate}" crate.

%package     -n %{name}+PermissionStatus-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PermissionStatus-devel

This package contains library source intended for building other packages which
use the "PermissionStatus" feature of the "%{crate}" crate.

%package     -n %{name}+Permissions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Permissions-devel

This package contains library source intended for building other packages which
use the "Permissions" feature of the "%{crate}" crate.

%package     -n %{name}+PhotoCapabilities-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PhotoCapabilities-devel

This package contains library source intended for building other packages which
use the "PhotoCapabilities" feature of the "%{crate}" crate.

%package     -n %{name}+PhotoSettings-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PhotoSettings-devel

This package contains library source intended for building other packages which
use the "PhotoSettings" feature of the "%{crate}" crate.

%package     -n %{name}+PictureInPictureEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PictureInPictureEvent-devel

This package contains library source intended for building other packages which
use the "PictureInPictureEvent" feature of the "%{crate}" crate.

%package     -n %{name}+PictureInPictureEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PictureInPictureEventInit-devel

This package contains library source intended for building other packages which
use the "PictureInPictureEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+PictureInPictureWindow-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PictureInPictureWindow-devel

This package contains library source intended for building other packages which
use the "PictureInPictureWindow" feature of the "%{crate}" crate.

%package     -n %{name}+PlaneLayout-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PlaneLayout-devel

This package contains library source intended for building other packages which
use the "PlaneLayout" feature of the "%{crate}" crate.

%package     -n %{name}+PlaybackDirection-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PlaybackDirection-devel

This package contains library source intended for building other packages which
use the "PlaybackDirection" feature of the "%{crate}" crate.

%package     -n %{name}+Plugin-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Plugin-devel

This package contains library source intended for building other packages which
use the "Plugin" feature of the "%{crate}" crate.

%package     -n %{name}+PluginArray-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PluginArray-devel

This package contains library source intended for building other packages which
use the "PluginArray" feature of the "%{crate}" crate.

%package     -n %{name}+PluginCrashedEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PluginCrashedEventInit-devel

This package contains library source intended for building other packages which
use the "PluginCrashedEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+Point2d-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Point2d-devel

This package contains library source intended for building other packages which
use the "Point2d" feature of the "%{crate}" crate.

%package     -n %{name}+PointerEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PointerEvent-devel

This package contains library source intended for building other packages which
use the "PointerEvent" feature of the "%{crate}" crate.

%package     -n %{name}+PointerEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PointerEventInit-devel

This package contains library source intended for building other packages which
use the "PointerEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+PopStateEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PopStateEvent-devel

This package contains library source intended for building other packages which
use the "PopStateEvent" feature of the "%{crate}" crate.

%package     -n %{name}+PopStateEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PopStateEventInit-devel

This package contains library source intended for building other packages which
use the "PopStateEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+PopupBlockedEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PopupBlockedEvent-devel

This package contains library source intended for building other packages which
use the "PopupBlockedEvent" feature of the "%{crate}" crate.

%package     -n %{name}+PopupBlockedEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PopupBlockedEventInit-devel

This package contains library source intended for building other packages which
use the "PopupBlockedEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+Position-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Position-devel

This package contains library source intended for building other packages which
use the "Position" feature of the "%{crate}" crate.

%package     -n %{name}+PositionAlignSetting-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PositionAlignSetting-devel

This package contains library source intended for building other packages which
use the "PositionAlignSetting" feature of the "%{crate}" crate.

%package     -n %{name}+PositionError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PositionError-devel

This package contains library source intended for building other packages which
use the "PositionError" feature of the "%{crate}" crate.

%package     -n %{name}+PositionOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PositionOptions-devel

This package contains library source intended for building other packages which
use the "PositionOptions" feature of the "%{crate}" crate.

%package     -n %{name}+PremultiplyAlpha-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PremultiplyAlpha-devel

This package contains library source intended for building other packages which
use the "PremultiplyAlpha" feature of the "%{crate}" crate.

%package     -n %{name}+Presentation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Presentation-devel

This package contains library source intended for building other packages which
use the "Presentation" feature of the "%{crate}" crate.

%package     -n %{name}+PresentationAvailability-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PresentationAvailability-devel

This package contains library source intended for building other packages which
use the "PresentationAvailability" feature of the "%{crate}" crate.

%package     -n %{name}+PresentationConnection-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PresentationConnection-devel

This package contains library source intended for building other packages which
use the "PresentationConnection" feature of the "%{crate}" crate.

%package     -n %{name}+PresentationConnectionAvailableEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PresentationConnectionAvailableEvent-devel

This package contains library source intended for building other packages which
use the "PresentationConnectionAvailableEvent" feature of the "%{crate}" crate.

%package     -n %{name}+PresentationConnectionAvailableEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PresentationConnectionAvailableEventInit-devel

This package contains library source intended for building other packages which
use the "PresentationConnectionAvailableEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+PresentationConnectionBinaryType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PresentationConnectionBinaryType-devel

This package contains library source intended for building other packages which
use the "PresentationConnectionBinaryType" feature of the "%{crate}" crate.

%package     -n %{name}+PresentationConnectionCloseEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PresentationConnectionCloseEvent-devel

This package contains library source intended for building other packages which
use the "PresentationConnectionCloseEvent" feature of the "%{crate}" crate.

%package     -n %{name}+PresentationConnectionCloseEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PresentationConnectionCloseEventInit-devel

This package contains library source intended for building other packages which
use the "PresentationConnectionCloseEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+PresentationConnectionClosedReason-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PresentationConnectionClosedReason-devel

This package contains library source intended for building other packages which
use the "PresentationConnectionClosedReason" feature of the "%{crate}" crate.

%package     -n %{name}+PresentationConnectionList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PresentationConnectionList-devel

This package contains library source intended for building other packages which
use the "PresentationConnectionList" feature of the "%{crate}" crate.

%package     -n %{name}+PresentationConnectionState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PresentationConnectionState-devel

This package contains library source intended for building other packages which
use the "PresentationConnectionState" feature of the "%{crate}" crate.

%package     -n %{name}+PresentationReceiver-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PresentationReceiver-devel

This package contains library source intended for building other packages which
use the "PresentationReceiver" feature of the "%{crate}" crate.

%package     -n %{name}+PresentationRequest-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PresentationRequest-devel

This package contains library source intended for building other packages which
use the "PresentationRequest" feature of the "%{crate}" crate.

%package     -n %{name}+PresentationStyle-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PresentationStyle-devel

This package contains library source intended for building other packages which
use the "PresentationStyle" feature of the "%{crate}" crate.

%package     -n %{name}+ProcessingInstruction-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ProcessingInstruction-devel

This package contains library source intended for building other packages which
use the "ProcessingInstruction" feature of the "%{crate}" crate.

%package     -n %{name}+ProfileTimelineLayerRect-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ProfileTimelineLayerRect-devel

This package contains library source intended for building other packages which
use the "ProfileTimelineLayerRect" feature of the "%{crate}" crate.

%package     -n %{name}+ProfileTimelineMarker-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ProfileTimelineMarker-devel

This package contains library source intended for building other packages which
use the "ProfileTimelineMarker" feature of the "%{crate}" crate.

%package     -n %{name}+ProfileTimelineMessagePortOperationType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ProfileTimelineMessagePortOperationType-devel

This package contains library source intended for building other packages which
use the "ProfileTimelineMessagePortOperationType" feature of the "%{crate}" crate.

%package     -n %{name}+ProfileTimelineStackFrame-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ProfileTimelineStackFrame-devel

This package contains library source intended for building other packages which
use the "ProfileTimelineStackFrame" feature of the "%{crate}" crate.

%package     -n %{name}+ProfileTimelineWorkerOperationType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ProfileTimelineWorkerOperationType-devel

This package contains library source intended for building other packages which
use the "ProfileTimelineWorkerOperationType" feature of the "%{crate}" crate.

%package     -n %{name}+ProgressEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ProgressEvent-devel

This package contains library source intended for building other packages which
use the "ProgressEvent" feature of the "%{crate}" crate.

%package     -n %{name}+ProgressEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ProgressEventInit-devel

This package contains library source intended for building other packages which
use the "ProgressEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+PromiseNativeHandler-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PromiseNativeHandler-devel

This package contains library source intended for building other packages which
use the "PromiseNativeHandler" feature of the "%{crate}" crate.

%package     -n %{name}+PromiseRejectionEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PromiseRejectionEvent-devel

This package contains library source intended for building other packages which
use the "PromiseRejectionEvent" feature of the "%{crate}" crate.

%package     -n %{name}+PromiseRejectionEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PromiseRejectionEventInit-devel

This package contains library source intended for building other packages which
use the "PromiseRejectionEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+PublicKeyCredential-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PublicKeyCredential-devel

This package contains library source intended for building other packages which
use the "PublicKeyCredential" feature of the "%{crate}" crate.

%package     -n %{name}+PublicKeyCredentialCreationOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PublicKeyCredentialCreationOptions-devel

This package contains library source intended for building other packages which
use the "PublicKeyCredentialCreationOptions" feature of the "%{crate}" crate.

%package     -n %{name}+PublicKeyCredentialCreationOptionsJson-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PublicKeyCredentialCreationOptionsJson-devel

This package contains library source intended for building other packages which
use the "PublicKeyCredentialCreationOptionsJson" feature of the "%{crate}" crate.

%package     -n %{name}+PublicKeyCredentialDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PublicKeyCredentialDescriptor-devel

This package contains library source intended for building other packages which
use the "PublicKeyCredentialDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+PublicKeyCredentialDescriptorJson-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PublicKeyCredentialDescriptorJson-devel

This package contains library source intended for building other packages which
use the "PublicKeyCredentialDescriptorJson" feature of the "%{crate}" crate.

%package     -n %{name}+PublicKeyCredentialEntity-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PublicKeyCredentialEntity-devel

This package contains library source intended for building other packages which
use the "PublicKeyCredentialEntity" feature of the "%{crate}" crate.

%package     -n %{name}+PublicKeyCredentialHints-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PublicKeyCredentialHints-devel

This package contains library source intended for building other packages which
use the "PublicKeyCredentialHints" feature of the "%{crate}" crate.

%package     -n %{name}+PublicKeyCredentialParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PublicKeyCredentialParameters-devel

This package contains library source intended for building other packages which
use the "PublicKeyCredentialParameters" feature of the "%{crate}" crate.

%package     -n %{name}+PublicKeyCredentialRequestOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PublicKeyCredentialRequestOptions-devel

This package contains library source intended for building other packages which
use the "PublicKeyCredentialRequestOptions" feature of the "%{crate}" crate.

%package     -n %{name}+PublicKeyCredentialRequestOptionsJson-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PublicKeyCredentialRequestOptionsJson-devel

This package contains library source intended for building other packages which
use the "PublicKeyCredentialRequestOptionsJson" feature of the "%{crate}" crate.

%package     -n %{name}+PublicKeyCredentialRpEntity-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PublicKeyCredentialRpEntity-devel

This package contains library source intended for building other packages which
use the "PublicKeyCredentialRpEntity" feature of the "%{crate}" crate.

%package     -n %{name}+PublicKeyCredentialType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PublicKeyCredentialType-devel

This package contains library source intended for building other packages which
use the "PublicKeyCredentialType" feature of the "%{crate}" crate.

%package     -n %{name}+PublicKeyCredentialUserEntity-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PublicKeyCredentialUserEntity-devel

This package contains library source intended for building other packages which
use the "PublicKeyCredentialUserEntity" feature of the "%{crate}" crate.

%package     -n %{name}+PublicKeyCredentialUserEntityJson-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PublicKeyCredentialUserEntityJson-devel

This package contains library source intended for building other packages which
use the "PublicKeyCredentialUserEntityJson" feature of the "%{crate}" crate.

%package     -n %{name}+PushEncryptionKeyName-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PushEncryptionKeyName-devel

This package contains library source intended for building other packages which
use the "PushEncryptionKeyName" feature of the "%{crate}" crate.

%package     -n %{name}+PushEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PushEvent-devel

This package contains library source intended for building other packages which
use the "PushEvent" feature of the "%{crate}" crate.

%package     -n %{name}+PushEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PushEventInit-devel

This package contains library source intended for building other packages which
use the "PushEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+PushManager-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PushManager-devel

This package contains library source intended for building other packages which
use the "PushManager" feature of the "%{crate}" crate.

%package     -n %{name}+PushMessageData-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PushMessageData-devel

This package contains library source intended for building other packages which
use the "PushMessageData" feature of the "%{crate}" crate.

%package     -n %{name}+PushPermissionState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PushPermissionState-devel

This package contains library source intended for building other packages which
use the "PushPermissionState" feature of the "%{crate}" crate.

%package     -n %{name}+PushSubscription-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PushSubscription-devel

This package contains library source intended for building other packages which
use the "PushSubscription" feature of the "%{crate}" crate.

%package     -n %{name}+PushSubscriptionInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PushSubscriptionInit-devel

This package contains library source intended for building other packages which
use the "PushSubscriptionInit" feature of the "%{crate}" crate.

%package     -n %{name}+PushSubscriptionJson-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PushSubscriptionJson-devel

This package contains library source intended for building other packages which
use the "PushSubscriptionJson" feature of the "%{crate}" crate.

%package     -n %{name}+PushSubscriptionKeys-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PushSubscriptionKeys-devel

This package contains library source intended for building other packages which
use the "PushSubscriptionKeys" feature of the "%{crate}" crate.

%package     -n %{name}+PushSubscriptionOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PushSubscriptionOptions-devel

This package contains library source intended for building other packages which
use the "PushSubscriptionOptions" feature of the "%{crate}" crate.

%package     -n %{name}+PushSubscriptionOptionsInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+PushSubscriptionOptionsInit-devel

This package contains library source intended for building other packages which
use the "PushSubscriptionOptionsInit" feature of the "%{crate}" crate.

%package     -n %{name}+QueryOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+QueryOptions-devel

This package contains library source intended for building other packages which
use the "QueryOptions" feature of the "%{crate}" crate.

%package     -n %{name}+QueuingStrategy-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+QueuingStrategy-devel

This package contains library source intended for building other packages which
use the "QueuingStrategy" feature of the "%{crate}" crate.

%package     -n %{name}+QueuingStrategyInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+QueuingStrategyInit-devel

This package contains library source intended for building other packages which
use the "QueuingStrategyInit" feature of the "%{crate}" crate.

%package     -n %{name}+RadioNodeList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RadioNodeList-devel

This package contains library source intended for building other packages which
use the "RadioNodeList" feature of the "%{crate}" crate.

%package     -n %{name}+Range-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Range-devel

This package contains library source intended for building other packages which
use the "Range" feature of the "%{crate}" crate.

%package     -n %{name}+RcwnPerfStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RcwnPerfStats-devel

This package contains library source intended for building other packages which
use the "RcwnPerfStats" feature of the "%{crate}" crate.

%package     -n %{name}+RcwnStatus-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RcwnStatus-devel

This package contains library source intended for building other packages which
use the "RcwnStatus" feature of the "%{crate}" crate.

%package     -n %{name}+ReadableByteStreamController-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ReadableByteStreamController-devel

This package contains library source intended for building other packages which
use the "ReadableByteStreamController" feature of the "%{crate}" crate.

%package     -n %{name}+ReadableStream-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ReadableStream-devel

This package contains library source intended for building other packages which
use the "ReadableStream" feature of the "%{crate}" crate.

%package     -n %{name}+ReadableStreamByobReader-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ReadableStreamByobReader-devel

This package contains library source intended for building other packages which
use the "ReadableStreamByobReader" feature of the "%{crate}" crate.

%package     -n %{name}+ReadableStreamByobRequest-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ReadableStreamByobRequest-devel

This package contains library source intended for building other packages which
use the "ReadableStreamByobRequest" feature of the "%{crate}" crate.

%package     -n %{name}+ReadableStreamDefaultController-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ReadableStreamDefaultController-devel

This package contains library source intended for building other packages which
use the "ReadableStreamDefaultController" feature of the "%{crate}" crate.

%package     -n %{name}+ReadableStreamDefaultReader-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ReadableStreamDefaultReader-devel

This package contains library source intended for building other packages which
use the "ReadableStreamDefaultReader" feature of the "%{crate}" crate.

%package     -n %{name}+ReadableStreamGetReaderOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ReadableStreamGetReaderOptions-devel

This package contains library source intended for building other packages which
use the "ReadableStreamGetReaderOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ReadableStreamIteratorOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ReadableStreamIteratorOptions-devel

This package contains library source intended for building other packages which
use the "ReadableStreamIteratorOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ReadableStreamReadResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ReadableStreamReadResult-devel

This package contains library source intended for building other packages which
use the "ReadableStreamReadResult" feature of the "%{crate}" crate.

%package     -n %{name}+ReadableStreamReaderMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ReadableStreamReaderMode-devel

This package contains library source intended for building other packages which
use the "ReadableStreamReaderMode" feature of the "%{crate}" crate.

%package     -n %{name}+ReadableStreamType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ReadableStreamType-devel

This package contains library source intended for building other packages which
use the "ReadableStreamType" feature of the "%{crate}" crate.

%package     -n %{name}+ReadableWritablePair-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ReadableWritablePair-devel

This package contains library source intended for building other packages which
use the "ReadableWritablePair" feature of the "%{crate}" crate.

%package     -n %{name}+RecordingState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RecordingState-devel

This package contains library source intended for building other packages which
use the "RecordingState" feature of the "%{crate}" crate.

%package     -n %{name}+RedEyeReduction-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RedEyeReduction-devel

This package contains library source intended for building other packages which
use the "RedEyeReduction" feature of the "%{crate}" crate.

%package     -n %{name}+ReferrerPolicy-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ReferrerPolicy-devel

This package contains library source intended for building other packages which
use the "ReferrerPolicy" feature of the "%{crate}" crate.

%package     -n %{name}+RegisterRequest-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RegisterRequest-devel

This package contains library source intended for building other packages which
use the "RegisterRequest" feature of the "%{crate}" crate.

%package     -n %{name}+RegisterResponse-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RegisterResponse-devel

This package contains library source intended for building other packages which
use the "RegisterResponse" feature of the "%{crate}" crate.

%package     -n %{name}+RegisteredKey-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RegisteredKey-devel

This package contains library source intended for building other packages which
use the "RegisteredKey" feature of the "%{crate}" crate.

%package     -n %{name}+RegistrationOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RegistrationOptions-devel

This package contains library source intended for building other packages which
use the "RegistrationOptions" feature of the "%{crate}" crate.

%package     -n %{name}+RegistrationResponseJson-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RegistrationResponseJson-devel

This package contains library source intended for building other packages which
use the "RegistrationResponseJson" feature of the "%{crate}" crate.

%package     -n %{name}+Request-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Request-devel

This package contains library source intended for building other packages which
use the "Request" feature of the "%{crate}" crate.

%package     -n %{name}+RequestCache-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RequestCache-devel

This package contains library source intended for building other packages which
use the "RequestCache" feature of the "%{crate}" crate.

%package     -n %{name}+RequestCredentials-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RequestCredentials-devel

This package contains library source intended for building other packages which
use the "RequestCredentials" feature of the "%{crate}" crate.

%package     -n %{name}+RequestDestination-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RequestDestination-devel

This package contains library source intended for building other packages which
use the "RequestDestination" feature of the "%{crate}" crate.

%package     -n %{name}+RequestDeviceOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RequestDeviceOptions-devel

This package contains library source intended for building other packages which
use the "RequestDeviceOptions" feature of the "%{crate}" crate.

%package     -n %{name}+RequestInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RequestInit-devel

This package contains library source intended for building other packages which
use the "RequestInit" feature of the "%{crate}" crate.

%package     -n %{name}+RequestMediaKeySystemAccessNotification-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RequestMediaKeySystemAccessNotification-devel

This package contains library source intended for building other packages which
use the "RequestMediaKeySystemAccessNotification" feature of the "%{crate}" crate.

%package     -n %{name}+RequestMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RequestMode-devel

This package contains library source intended for building other packages which
use the "RequestMode" feature of the "%{crate}" crate.

%package     -n %{name}+RequestRedirect-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RequestRedirect-devel

This package contains library source intended for building other packages which
use the "RequestRedirect" feature of the "%{crate}" crate.

%package     -n %{name}+ResidentKeyRequirement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ResidentKeyRequirement-devel

This package contains library source intended for building other packages which
use the "ResidentKeyRequirement" feature of the "%{crate}" crate.

%package     -n %{name}+ResizeObserver-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ResizeObserver-devel

This package contains library source intended for building other packages which
use the "ResizeObserver" feature of the "%{crate}" crate.

%package     -n %{name}+ResizeObserverBoxOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ResizeObserverBoxOptions-devel

This package contains library source intended for building other packages which
use the "ResizeObserverBoxOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ResizeObserverEntry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ResizeObserverEntry-devel

This package contains library source intended for building other packages which
use the "ResizeObserverEntry" feature of the "%{crate}" crate.

%package     -n %{name}+ResizeObserverOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ResizeObserverOptions-devel

This package contains library source intended for building other packages which
use the "ResizeObserverOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ResizeObserverSize-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ResizeObserverSize-devel

This package contains library source intended for building other packages which
use the "ResizeObserverSize" feature of the "%{crate}" crate.

%package     -n %{name}+ResizeQuality-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ResizeQuality-devel

This package contains library source intended for building other packages which
use the "ResizeQuality" feature of the "%{crate}" crate.

%package     -n %{name}+Response-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Response-devel

This package contains library source intended for building other packages which
use the "Response" feature of the "%{crate}" crate.

%package     -n %{name}+ResponseInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ResponseInit-devel

This package contains library source intended for building other packages which
use the "ResponseInit" feature of the "%{crate}" crate.

%package     -n %{name}+ResponseType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ResponseType-devel

This package contains library source intended for building other packages which
use the "ResponseType" feature of the "%{crate}" crate.

%package     -n %{name}+RsaHashedImportParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RsaHashedImportParams-devel

This package contains library source intended for building other packages which
use the "RsaHashedImportParams" feature of the "%{crate}" crate.

%package     -n %{name}+RsaOaepParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RsaOaepParams-devel

This package contains library source intended for building other packages which
use the "RsaOaepParams" feature of the "%{crate}" crate.

%package     -n %{name}+RsaOtherPrimesInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RsaOtherPrimesInfo-devel

This package contains library source intended for building other packages which
use the "RsaOtherPrimesInfo" feature of the "%{crate}" crate.

%package     -n %{name}+RsaPssParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RsaPssParams-devel

This package contains library source intended for building other packages which
use the "RsaPssParams" feature of the "%{crate}" crate.

%package     -n %{name}+RtcAnswerOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcAnswerOptions-devel

This package contains library source intended for building other packages which
use the "RtcAnswerOptions" feature of the "%{crate}" crate.

%package     -n %{name}+RtcBundlePolicy-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcBundlePolicy-devel

This package contains library source intended for building other packages which
use the "RtcBundlePolicy" feature of the "%{crate}" crate.

%package     -n %{name}+RtcCertificate-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcCertificate-devel

This package contains library source intended for building other packages which
use the "RtcCertificate" feature of the "%{crate}" crate.

%package     -n %{name}+RtcCertificateExpiration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcCertificateExpiration-devel

This package contains library source intended for building other packages which
use the "RtcCertificateExpiration" feature of the "%{crate}" crate.

%package     -n %{name}+RtcCodecStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcCodecStats-devel

This package contains library source intended for building other packages which
use the "RtcCodecStats" feature of the "%{crate}" crate.

%package     -n %{name}+RtcConfiguration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcConfiguration-devel

This package contains library source intended for building other packages which
use the "RtcConfiguration" feature of the "%{crate}" crate.

%package     -n %{name}+RtcDataChannel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcDataChannel-devel

This package contains library source intended for building other packages which
use the "RtcDataChannel" feature of the "%{crate}" crate.

%package     -n %{name}+RtcDataChannelEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcDataChannelEvent-devel

This package contains library source intended for building other packages which
use the "RtcDataChannelEvent" feature of the "%{crate}" crate.

%package     -n %{name}+RtcDataChannelEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcDataChannelEventInit-devel

This package contains library source intended for building other packages which
use the "RtcDataChannelEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+RtcDataChannelInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcDataChannelInit-devel

This package contains library source intended for building other packages which
use the "RtcDataChannelInit" feature of the "%{crate}" crate.

%package     -n %{name}+RtcDataChannelState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcDataChannelState-devel

This package contains library source intended for building other packages which
use the "RtcDataChannelState" feature of the "%{crate}" crate.

%package     -n %{name}+RtcDataChannelType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcDataChannelType-devel

This package contains library source intended for building other packages which
use the "RtcDataChannelType" feature of the "%{crate}" crate.

%package     -n %{name}+RtcDegradationPreference-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcDegradationPreference-devel

This package contains library source intended for building other packages which
use the "RtcDegradationPreference" feature of the "%{crate}" crate.

%package     -n %{name}+RtcEncodedAudioFrame-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcEncodedAudioFrame-devel

This package contains library source intended for building other packages which
use the "RtcEncodedAudioFrame" feature of the "%{crate}" crate.

%package     -n %{name}+RtcEncodedAudioFrameMetadata-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcEncodedAudioFrameMetadata-devel

This package contains library source intended for building other packages which
use the "RtcEncodedAudioFrameMetadata" feature of the "%{crate}" crate.

%package     -n %{name}+RtcEncodedAudioFrameOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcEncodedAudioFrameOptions-devel

This package contains library source intended for building other packages which
use the "RtcEncodedAudioFrameOptions" feature of the "%{crate}" crate.

%package     -n %{name}+RtcEncodedVideoFrame-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcEncodedVideoFrame-devel

This package contains library source intended for building other packages which
use the "RtcEncodedVideoFrame" feature of the "%{crate}" crate.

%package     -n %{name}+RtcEncodedVideoFrameMetadata-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcEncodedVideoFrameMetadata-devel

This package contains library source intended for building other packages which
use the "RtcEncodedVideoFrameMetadata" feature of the "%{crate}" crate.

%package     -n %{name}+RtcEncodedVideoFrameOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcEncodedVideoFrameOptions-devel

This package contains library source intended for building other packages which
use the "RtcEncodedVideoFrameOptions" feature of the "%{crate}" crate.

%package     -n %{name}+RtcEncodedVideoFrameType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcEncodedVideoFrameType-devel

This package contains library source intended for building other packages which
use the "RtcEncodedVideoFrameType" feature of the "%{crate}" crate.

%package     -n %{name}+RtcFecParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcFecParameters-devel

This package contains library source intended for building other packages which
use the "RtcFecParameters" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIceCandidate-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIceCandidate-devel

This package contains library source intended for building other packages which
use the "RtcIceCandidate" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIceCandidateInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIceCandidateInit-devel

This package contains library source intended for building other packages which
use the "RtcIceCandidateInit" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIceCandidatePairStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIceCandidatePairStats-devel

This package contains library source intended for building other packages which
use the "RtcIceCandidatePairStats" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIceCandidateStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIceCandidateStats-devel

This package contains library source intended for building other packages which
use the "RtcIceCandidateStats" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIceComponentStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIceComponentStats-devel

This package contains library source intended for building other packages which
use the "RtcIceComponentStats" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIceConnectionState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIceConnectionState-devel

This package contains library source intended for building other packages which
use the "RtcIceConnectionState" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIceCredentialType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIceCredentialType-devel

This package contains library source intended for building other packages which
use the "RtcIceCredentialType" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIceGatheringState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIceGatheringState-devel

This package contains library source intended for building other packages which
use the "RtcIceGatheringState" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIceServer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIceServer-devel

This package contains library source intended for building other packages which
use the "RtcIceServer" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIceTransportPolicy-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIceTransportPolicy-devel

This package contains library source intended for building other packages which
use the "RtcIceTransportPolicy" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIdentityAssertion-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIdentityAssertion-devel

This package contains library source intended for building other packages which
use the "RtcIdentityAssertion" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIdentityAssertionResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIdentityAssertionResult-devel

This package contains library source intended for building other packages which
use the "RtcIdentityAssertionResult" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIdentityProvider-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIdentityProvider-devel

This package contains library source intended for building other packages which
use the "RtcIdentityProvider" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIdentityProviderDetails-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIdentityProviderDetails-devel

This package contains library source intended for building other packages which
use the "RtcIdentityProviderDetails" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIdentityProviderOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIdentityProviderOptions-devel

This package contains library source intended for building other packages which
use the "RtcIdentityProviderOptions" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIdentityProviderRegistrar-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIdentityProviderRegistrar-devel

This package contains library source intended for building other packages which
use the "RtcIdentityProviderRegistrar" feature of the "%{crate}" crate.

%package     -n %{name}+RtcIdentityValidationResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcIdentityValidationResult-devel

This package contains library source intended for building other packages which
use the "RtcIdentityValidationResult" feature of the "%{crate}" crate.

%package     -n %{name}+RtcInboundRtpStreamStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcInboundRtpStreamStats-devel

This package contains library source intended for building other packages which
use the "RtcInboundRtpStreamStats" feature of the "%{crate}" crate.

%package     -n %{name}+RtcMediaStreamStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcMediaStreamStats-devel

This package contains library source intended for building other packages which
use the "RtcMediaStreamStats" feature of the "%{crate}" crate.

%package     -n %{name}+RtcMediaStreamTrackStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcMediaStreamTrackStats-devel

This package contains library source intended for building other packages which
use the "RtcMediaStreamTrackStats" feature of the "%{crate}" crate.

%package     -n %{name}+RtcOfferAnswerOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcOfferAnswerOptions-devel

This package contains library source intended for building other packages which
use the "RtcOfferAnswerOptions" feature of the "%{crate}" crate.

%package     -n %{name}+RtcOfferOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcOfferOptions-devel

This package contains library source intended for building other packages which
use the "RtcOfferOptions" feature of the "%{crate}" crate.

%package     -n %{name}+RtcOutboundRtpStreamStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcOutboundRtpStreamStats-devel

This package contains library source intended for building other packages which
use the "RtcOutboundRtpStreamStats" feature of the "%{crate}" crate.

%package     -n %{name}+RtcPeerConnection-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcPeerConnection-devel

This package contains library source intended for building other packages which
use the "RtcPeerConnection" feature of the "%{crate}" crate.

%package     -n %{name}+RtcPeerConnectionIceErrorEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcPeerConnectionIceErrorEvent-devel

This package contains library source intended for building other packages which
use the "RtcPeerConnectionIceErrorEvent" feature of the "%{crate}" crate.

%package     -n %{name}+RtcPeerConnectionIceEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcPeerConnectionIceEvent-devel

This package contains library source intended for building other packages which
use the "RtcPeerConnectionIceEvent" feature of the "%{crate}" crate.

%package     -n %{name}+RtcPeerConnectionIceEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcPeerConnectionIceEventInit-devel

This package contains library source intended for building other packages which
use the "RtcPeerConnectionIceEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+RtcPeerConnectionState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcPeerConnectionState-devel

This package contains library source intended for building other packages which
use the "RtcPeerConnectionState" feature of the "%{crate}" crate.

%package     -n %{name}+RtcPriorityType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcPriorityType-devel

This package contains library source intended for building other packages which
use the "RtcPriorityType" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtcpParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtcpParameters-devel

This package contains library source intended for building other packages which
use the "RtcRtcpParameters" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpCapabilities-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpCapabilities-devel

This package contains library source intended for building other packages which
use the "RtcRtpCapabilities" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpCodecCapability-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpCodecCapability-devel

This package contains library source intended for building other packages which
use the "RtcRtpCodecCapability" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpCodecParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpCodecParameters-devel

This package contains library source intended for building other packages which
use the "RtcRtpCodecParameters" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpContributingSource-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpContributingSource-devel

This package contains library source intended for building other packages which
use the "RtcRtpContributingSource" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpEncodingParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpEncodingParameters-devel

This package contains library source intended for building other packages which
use the "RtcRtpEncodingParameters" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpHeaderExtensionCapability-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpHeaderExtensionCapability-devel

This package contains library source intended for building other packages which
use the "RtcRtpHeaderExtensionCapability" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpHeaderExtensionParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpHeaderExtensionParameters-devel

This package contains library source intended for building other packages which
use the "RtcRtpHeaderExtensionParameters" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpParameters-devel

This package contains library source intended for building other packages which
use the "RtcRtpParameters" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpReceiver-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpReceiver-devel

This package contains library source intended for building other packages which
use the "RtcRtpReceiver" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpScriptTransform-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpScriptTransform-devel

This package contains library source intended for building other packages which
use the "RtcRtpScriptTransform" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpScriptTransformer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpScriptTransformer-devel

This package contains library source intended for building other packages which
use the "RtcRtpScriptTransformer" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpSender-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpSender-devel

This package contains library source intended for building other packages which
use the "RtcRtpSender" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpSourceEntry-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpSourceEntry-devel

This package contains library source intended for building other packages which
use the "RtcRtpSourceEntry" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpSourceEntryType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpSourceEntryType-devel

This package contains library source intended for building other packages which
use the "RtcRtpSourceEntryType" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpSynchronizationSource-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpSynchronizationSource-devel

This package contains library source intended for building other packages which
use the "RtcRtpSynchronizationSource" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpTransceiver-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpTransceiver-devel

This package contains library source intended for building other packages which
use the "RtcRtpTransceiver" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpTransceiverDirection-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpTransceiverDirection-devel

This package contains library source intended for building other packages which
use the "RtcRtpTransceiverDirection" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtpTransceiverInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtpTransceiverInit-devel

This package contains library source intended for building other packages which
use the "RtcRtpTransceiverInit" feature of the "%{crate}" crate.

%package     -n %{name}+RtcRtxParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcRtxParameters-devel

This package contains library source intended for building other packages which
use the "RtcRtxParameters" feature of the "%{crate}" crate.

%package     -n %{name}+RtcSdpType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcSdpType-devel

This package contains library source intended for building other packages which
use the "RtcSdpType" feature of the "%{crate}" crate.

%package     -n %{name}+RtcSessionDescription-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcSessionDescription-devel

This package contains library source intended for building other packages which
use the "RtcSessionDescription" feature of the "%{crate}" crate.

%package     -n %{name}+RtcSessionDescriptionInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcSessionDescriptionInit-devel

This package contains library source intended for building other packages which
use the "RtcSessionDescriptionInit" feature of the "%{crate}" crate.

%package     -n %{name}+RtcSignalingState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcSignalingState-devel

This package contains library source intended for building other packages which
use the "RtcSignalingState" feature of the "%{crate}" crate.

%package     -n %{name}+RtcStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcStats-devel

This package contains library source intended for building other packages which
use the "RtcStats" feature of the "%{crate}" crate.

%package     -n %{name}+RtcStatsIceCandidatePairState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcStatsIceCandidatePairState-devel

This package contains library source intended for building other packages which
use the "RtcStatsIceCandidatePairState" feature of the "%{crate}" crate.

%package     -n %{name}+RtcStatsIceCandidateType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcStatsIceCandidateType-devel

This package contains library source intended for building other packages which
use the "RtcStatsIceCandidateType" feature of the "%{crate}" crate.

%package     -n %{name}+RtcStatsReport-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcStatsReport-devel

This package contains library source intended for building other packages which
use the "RtcStatsReport" feature of the "%{crate}" crate.

%package     -n %{name}+RtcStatsReportInternal-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcStatsReportInternal-devel

This package contains library source intended for building other packages which
use the "RtcStatsReportInternal" feature of the "%{crate}" crate.

%package     -n %{name}+RtcStatsType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcStatsType-devel

This package contains library source intended for building other packages which
use the "RtcStatsType" feature of the "%{crate}" crate.

%package     -n %{name}+RtcTrackEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcTrackEvent-devel

This package contains library source intended for building other packages which
use the "RtcTrackEvent" feature of the "%{crate}" crate.

%package     -n %{name}+RtcTrackEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcTrackEventInit-devel

This package contains library source intended for building other packages which
use the "RtcTrackEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+RtcTransformEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcTransformEvent-devel

This package contains library source intended for building other packages which
use the "RtcTransformEvent" feature of the "%{crate}" crate.

%package     -n %{name}+RtcTransportStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcTransportStats-devel

This package contains library source intended for building other packages which
use the "RtcTransportStats" feature of the "%{crate}" crate.

%package     -n %{name}+RtcdtmfSender-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcdtmfSender-devel

This package contains library source intended for building other packages which
use the "RtcdtmfSender" feature of the "%{crate}" crate.

%package     -n %{name}+RtcdtmfToneChangeEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcdtmfToneChangeEvent-devel

This package contains library source intended for building other packages which
use the "RtcdtmfToneChangeEvent" feature of the "%{crate}" crate.

%package     -n %{name}+RtcdtmfToneChangeEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcdtmfToneChangeEventInit-devel

This package contains library source intended for building other packages which
use the "RtcdtmfToneChangeEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+RtcrtpContributingSourceStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcrtpContributingSourceStats-devel

This package contains library source intended for building other packages which
use the "RtcrtpContributingSourceStats" feature of the "%{crate}" crate.

%package     -n %{name}+RtcrtpStreamStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+RtcrtpStreamStats-devel

This package contains library source intended for building other packages which
use the "RtcrtpStreamStats" feature of the "%{crate}" crate.

%package     -n %{name}+SFrameTransform-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SFrameTransform-devel

This package contains library source intended for building other packages which
use the "SFrameTransform" feature of the "%{crate}" crate.

%package     -n %{name}+SFrameTransformErrorEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SFrameTransformErrorEvent-devel

This package contains library source intended for building other packages which
use the "SFrameTransformErrorEvent" feature of the "%{crate}" crate.

%package     -n %{name}+SFrameTransformErrorEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SFrameTransformErrorEventInit-devel

This package contains library source intended for building other packages which
use the "SFrameTransformErrorEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+SFrameTransformErrorEventType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SFrameTransformErrorEventType-devel

This package contains library source intended for building other packages which
use the "SFrameTransformErrorEventType" feature of the "%{crate}" crate.

%package     -n %{name}+SFrameTransformOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SFrameTransformOptions-devel

This package contains library source intended for building other packages which
use the "SFrameTransformOptions" feature of the "%{crate}" crate.

%package     -n %{name}+SFrameTransformRole-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SFrameTransformRole-devel

This package contains library source intended for building other packages which
use the "SFrameTransformRole" feature of the "%{crate}" crate.

%package     -n %{name}+SaveFilePickerOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SaveFilePickerOptions-devel

This package contains library source intended for building other packages which
use the "SaveFilePickerOptions" feature of the "%{crate}" crate.

%package     -n %{name}+Scheduler-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Scheduler-devel

This package contains library source intended for building other packages which
use the "Scheduler" feature of the "%{crate}" crate.

%package     -n %{name}+SchedulerPostTaskOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SchedulerPostTaskOptions-devel

This package contains library source intended for building other packages which
use the "SchedulerPostTaskOptions" feature of the "%{crate}" crate.

%package     -n %{name}+Scheduling-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Scheduling-devel

This package contains library source intended for building other packages which
use the "Scheduling" feature of the "%{crate}" crate.

%package     -n %{name}+Screen-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Screen-devel

This package contains library source intended for building other packages which
use the "Screen" feature of the "%{crate}" crate.

%package     -n %{name}+ScreenColorGamut-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScreenColorGamut-devel

This package contains library source intended for building other packages which
use the "ScreenColorGamut" feature of the "%{crate}" crate.

%package     -n %{name}+ScreenDetailed-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScreenDetailed-devel

This package contains library source intended for building other packages which
use the "ScreenDetailed" feature of the "%{crate}" crate.

%package     -n %{name}+ScreenDetails-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScreenDetails-devel

This package contains library source intended for building other packages which
use the "ScreenDetails" feature of the "%{crate}" crate.

%package     -n %{name}+ScreenLuminance-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScreenLuminance-devel

This package contains library source intended for building other packages which
use the "ScreenLuminance" feature of the "%{crate}" crate.

%package     -n %{name}+ScreenOrientation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScreenOrientation-devel

This package contains library source intended for building other packages which
use the "ScreenOrientation" feature of the "%{crate}" crate.

%package     -n %{name}+ScriptProcessorNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScriptProcessorNode-devel

This package contains library source intended for building other packages which
use the "ScriptProcessorNode" feature of the "%{crate}" crate.

%package     -n %{name}+ScrollAreaEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScrollAreaEvent-devel

This package contains library source intended for building other packages which
use the "ScrollAreaEvent" feature of the "%{crate}" crate.

%package     -n %{name}+ScrollBehavior-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScrollBehavior-devel

This package contains library source intended for building other packages which
use the "ScrollBehavior" feature of the "%{crate}" crate.

%package     -n %{name}+ScrollBoxObject-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScrollBoxObject-devel

This package contains library source intended for building other packages which
use the "ScrollBoxObject" feature of the "%{crate}" crate.

%package     -n %{name}+ScrollIntoViewContainer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScrollIntoViewContainer-devel

This package contains library source intended for building other packages which
use the "ScrollIntoViewContainer" feature of the "%{crate}" crate.

%package     -n %{name}+ScrollIntoViewOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScrollIntoViewOptions-devel

This package contains library source intended for building other packages which
use the "ScrollIntoViewOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ScrollLogicalPosition-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScrollLogicalPosition-devel

This package contains library source intended for building other packages which
use the "ScrollLogicalPosition" feature of the "%{crate}" crate.

%package     -n %{name}+ScrollOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScrollOptions-devel

This package contains library source intended for building other packages which
use the "ScrollOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ScrollRestoration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScrollRestoration-devel

This package contains library source intended for building other packages which
use the "ScrollRestoration" feature of the "%{crate}" crate.

%package     -n %{name}+ScrollSetting-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScrollSetting-devel

This package contains library source intended for building other packages which
use the "ScrollSetting" feature of the "%{crate}" crate.

%package     -n %{name}+ScrollState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScrollState-devel

This package contains library source intended for building other packages which
use the "ScrollState" feature of the "%{crate}" crate.

%package     -n %{name}+ScrollToOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScrollToOptions-devel

This package contains library source intended for building other packages which
use the "ScrollToOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ScrollViewChangeEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ScrollViewChangeEventInit-devel

This package contains library source intended for building other packages which
use the "ScrollViewChangeEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+SecurityPolicyViolationEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SecurityPolicyViolationEvent-devel

This package contains library source intended for building other packages which
use the "SecurityPolicyViolationEvent" feature of the "%{crate}" crate.

%package     -n %{name}+SecurityPolicyViolationEventDisposition-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SecurityPolicyViolationEventDisposition-devel

This package contains library source intended for building other packages which
use the "SecurityPolicyViolationEventDisposition" feature of the "%{crate}" crate.

%package     -n %{name}+SecurityPolicyViolationEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SecurityPolicyViolationEventInit-devel

This package contains library source intended for building other packages which
use the "SecurityPolicyViolationEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+Selection-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Selection-devel

This package contains library source intended for building other packages which
use the "Selection" feature of the "%{crate}" crate.

%package     -n %{name}+SelectionMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SelectionMode-devel

This package contains library source intended for building other packages which
use the "SelectionMode" feature of the "%{crate}" crate.

%package     -n %{name}+Serial-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Serial-devel

This package contains library source intended for building other packages which
use the "Serial" feature of the "%{crate}" crate.

%package     -n %{name}+SerialInputSignals-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SerialInputSignals-devel

This package contains library source intended for building other packages which
use the "SerialInputSignals" feature of the "%{crate}" crate.

%package     -n %{name}+SerialOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SerialOptions-devel

This package contains library source intended for building other packages which
use the "SerialOptions" feature of the "%{crate}" crate.

%package     -n %{name}+SerialOutputSignals-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SerialOutputSignals-devel

This package contains library source intended for building other packages which
use the "SerialOutputSignals" feature of the "%{crate}" crate.

%package     -n %{name}+SerialPort-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SerialPort-devel

This package contains library source intended for building other packages which
use the "SerialPort" feature of the "%{crate}" crate.

%package     -n %{name}+SerialPortFilter-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SerialPortFilter-devel

This package contains library source intended for building other packages which
use the "SerialPortFilter" feature of the "%{crate}" crate.

%package     -n %{name}+SerialPortInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SerialPortInfo-devel

This package contains library source intended for building other packages which
use the "SerialPortInfo" feature of the "%{crate}" crate.

%package     -n %{name}+SerialPortRequestOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SerialPortRequestOptions-devel

This package contains library source intended for building other packages which
use the "SerialPortRequestOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ServerSocketOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ServerSocketOptions-devel

This package contains library source intended for building other packages which
use the "ServerSocketOptions" feature of the "%{crate}" crate.

%package     -n %{name}+ServiceWorker-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ServiceWorker-devel

This package contains library source intended for building other packages which
use the "ServiceWorker" feature of the "%{crate}" crate.

%package     -n %{name}+ServiceWorkerContainer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ServiceWorkerContainer-devel

This package contains library source intended for building other packages which
use the "ServiceWorkerContainer" feature of the "%{crate}" crate.

%package     -n %{name}+ServiceWorkerGlobalScope-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ServiceWorkerGlobalScope-devel

This package contains library source intended for building other packages which
use the "ServiceWorkerGlobalScope" feature of the "%{crate}" crate.

%package     -n %{name}+ServiceWorkerRegistration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ServiceWorkerRegistration-devel

This package contains library source intended for building other packages which
use the "ServiceWorkerRegistration" feature of the "%{crate}" crate.

%package     -n %{name}+ServiceWorkerState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ServiceWorkerState-devel

This package contains library source intended for building other packages which
use the "ServiceWorkerState" feature of the "%{crate}" crate.

%package     -n %{name}+ServiceWorkerUpdateViaCache-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ServiceWorkerUpdateViaCache-devel

This package contains library source intended for building other packages which
use the "ServiceWorkerUpdateViaCache" feature of the "%{crate}" crate.

%package     -n %{name}+ShadowRoot-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ShadowRoot-devel

This package contains library source intended for building other packages which
use the "ShadowRoot" feature of the "%{crate}" crate.

%package     -n %{name}+ShadowRootInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ShadowRootInit-devel

This package contains library source intended for building other packages which
use the "ShadowRootInit" feature of the "%{crate}" crate.

%package     -n %{name}+ShadowRootMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ShadowRootMode-devel

This package contains library source intended for building other packages which
use the "ShadowRootMode" feature of the "%{crate}" crate.

%package     -n %{name}+ShareData-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ShareData-devel

This package contains library source intended for building other packages which
use the "ShareData" feature of the "%{crate}" crate.

%package     -n %{name}+SharedWorker-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SharedWorker-devel

This package contains library source intended for building other packages which
use the "SharedWorker" feature of the "%{crate}" crate.

%package     -n %{name}+SharedWorkerGlobalScope-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SharedWorkerGlobalScope-devel

This package contains library source intended for building other packages which
use the "SharedWorkerGlobalScope" feature of the "%{crate}" crate.

%package     -n %{name}+ShowPopoverOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ShowPopoverOptions-devel

This package contains library source intended for building other packages which
use the "ShowPopoverOptions" feature of the "%{crate}" crate.

%package     -n %{name}+SignResponse-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SignResponse-devel

This package contains library source intended for building other packages which
use the "SignResponse" feature of the "%{crate}" crate.

%package     -n %{name}+SocketElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SocketElement-devel

This package contains library source intended for building other packages which
use the "SocketElement" feature of the "%{crate}" crate.

%package     -n %{name}+SocketOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SocketOptions-devel

This package contains library source intended for building other packages which
use the "SocketOptions" feature of the "%{crate}" crate.

%package     -n %{name}+SocketReadyState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SocketReadyState-devel

This package contains library source intended for building other packages which
use the "SocketReadyState" feature of the "%{crate}" crate.

%package     -n %{name}+SocketsDict-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SocketsDict-devel

This package contains library source intended for building other packages which
use the "SocketsDict" feature of the "%{crate}" crate.

%package     -n %{name}+SourceBuffer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SourceBuffer-devel

This package contains library source intended for building other packages which
use the "SourceBuffer" feature of the "%{crate}" crate.

%package     -n %{name}+SourceBufferAppendMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SourceBufferAppendMode-devel

This package contains library source intended for building other packages which
use the "SourceBufferAppendMode" feature of the "%{crate}" crate.

%package     -n %{name}+SourceBufferList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SourceBufferList-devel

This package contains library source intended for building other packages which
use the "SourceBufferList" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechGrammar-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechGrammar-devel

This package contains library source intended for building other packages which
use the "SpeechGrammar" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechGrammarList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechGrammarList-devel

This package contains library source intended for building other packages which
use the "SpeechGrammarList" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechRecognition-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechRecognition-devel

This package contains library source intended for building other packages which
use the "SpeechRecognition" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechRecognitionAlternative-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechRecognitionAlternative-devel

This package contains library source intended for building other packages which
use the "SpeechRecognitionAlternative" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechRecognitionError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechRecognitionError-devel

This package contains library source intended for building other packages which
use the "SpeechRecognitionError" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechRecognitionErrorCode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechRecognitionErrorCode-devel

This package contains library source intended for building other packages which
use the "SpeechRecognitionErrorCode" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechRecognitionErrorInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechRecognitionErrorInit-devel

This package contains library source intended for building other packages which
use the "SpeechRecognitionErrorInit" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechRecognitionEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechRecognitionEvent-devel

This package contains library source intended for building other packages which
use the "SpeechRecognitionEvent" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechRecognitionEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechRecognitionEventInit-devel

This package contains library source intended for building other packages which
use the "SpeechRecognitionEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechRecognitionResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechRecognitionResult-devel

This package contains library source intended for building other packages which
use the "SpeechRecognitionResult" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechRecognitionResultList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechRecognitionResultList-devel

This package contains library source intended for building other packages which
use the "SpeechRecognitionResultList" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechSynthesis-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechSynthesis-devel

This package contains library source intended for building other packages which
use the "SpeechSynthesis" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechSynthesisErrorCode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechSynthesisErrorCode-devel

This package contains library source intended for building other packages which
use the "SpeechSynthesisErrorCode" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechSynthesisErrorEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechSynthesisErrorEvent-devel

This package contains library source intended for building other packages which
use the "SpeechSynthesisErrorEvent" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechSynthesisErrorEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechSynthesisErrorEventInit-devel

This package contains library source intended for building other packages which
use the "SpeechSynthesisErrorEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechSynthesisEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechSynthesisEvent-devel

This package contains library source intended for building other packages which
use the "SpeechSynthesisEvent" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechSynthesisEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechSynthesisEventInit-devel

This package contains library source intended for building other packages which
use the "SpeechSynthesisEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechSynthesisUtterance-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechSynthesisUtterance-devel

This package contains library source intended for building other packages which
use the "SpeechSynthesisUtterance" feature of the "%{crate}" crate.

%package     -n %{name}+SpeechSynthesisVoice-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SpeechSynthesisVoice-devel

This package contains library source intended for building other packages which
use the "SpeechSynthesisVoice" feature of the "%{crate}" crate.

%package     -n %{name}+StartViewTransitionOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StartViewTransitionOptions-devel

This package contains library source intended for building other packages which
use the "StartViewTransitionOptions" feature of the "%{crate}" crate.

%package     -n %{name}+StaticRange-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StaticRange-devel

This package contains library source intended for building other packages which
use the "StaticRange" feature of the "%{crate}" crate.

%package     -n %{name}+StaticRangeInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StaticRangeInit-devel

This package contains library source intended for building other packages which
use the "StaticRangeInit" feature of the "%{crate}" crate.

%package     -n %{name}+StereoPannerNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StereoPannerNode-devel

This package contains library source intended for building other packages which
use the "StereoPannerNode" feature of the "%{crate}" crate.

%package     -n %{name}+StereoPannerOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StereoPannerOptions-devel

This package contains library source intended for building other packages which
use the "StereoPannerOptions" feature of the "%{crate}" crate.

%package     -n %{name}+Storage-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Storage-devel

This package contains library source intended for building other packages which
use the "Storage" feature of the "%{crate}" crate.

%package     -n %{name}+StorageEstimate-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StorageEstimate-devel

This package contains library source intended for building other packages which
use the "StorageEstimate" feature of the "%{crate}" crate.

%package     -n %{name}+StorageEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StorageEvent-devel

This package contains library source intended for building other packages which
use the "StorageEvent" feature of the "%{crate}" crate.

%package     -n %{name}+StorageEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StorageEventInit-devel

This package contains library source intended for building other packages which
use the "StorageEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+StorageManager-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StorageManager-devel

This package contains library source intended for building other packages which
use the "StorageManager" feature of the "%{crate}" crate.

%package     -n %{name}+StorageType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StorageType-devel

This package contains library source intended for building other packages which
use the "StorageType" feature of the "%{crate}" crate.

%package     -n %{name}+StreamPipeOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StreamPipeOptions-devel

This package contains library source intended for building other packages which
use the "StreamPipeOptions" feature of the "%{crate}" crate.

%package     -n %{name}+StyleRuleChangeEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StyleRuleChangeEventInit-devel

This package contains library source intended for building other packages which
use the "StyleRuleChangeEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+StyleSheet-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StyleSheet-devel

This package contains library source intended for building other packages which
use the "StyleSheet" feature of the "%{crate}" crate.

%package     -n %{name}+StyleSheetApplicableStateChangeEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StyleSheetApplicableStateChangeEventInit-devel

This package contains library source intended for building other packages which
use the "StyleSheetApplicableStateChangeEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+StyleSheetChangeEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StyleSheetChangeEventInit-devel

This package contains library source intended for building other packages which
use the "StyleSheetChangeEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+StyleSheetList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+StyleSheetList-devel

This package contains library source intended for building other packages which
use the "StyleSheetList" feature of the "%{crate}" crate.

%package     -n %{name}+SubmitEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SubmitEvent-devel

This package contains library source intended for building other packages which
use the "SubmitEvent" feature of the "%{crate}" crate.

%package     -n %{name}+SubmitEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SubmitEventInit-devel

This package contains library source intended for building other packages which
use the "SubmitEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+SubtleCrypto-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SubtleCrypto-devel

This package contains library source intended for building other packages which
use the "SubtleCrypto" feature of the "%{crate}" crate.

%package     -n %{name}+SupportedType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SupportedType-devel

This package contains library source intended for building other packages which
use the "SupportedType" feature of the "%{crate}" crate.

%package     -n %{name}+SvcOutputMetadata-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvcOutputMetadata-devel

This package contains library source intended for building other packages which
use the "SvcOutputMetadata" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAngle-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAngle-devel

This package contains library source intended for building other packages which
use the "SvgAngle" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimateElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimateElement-devel

This package contains library source intended for building other packages which
use the "SvgAnimateElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimateMotionElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimateMotionElement-devel

This package contains library source intended for building other packages which
use the "SvgAnimateMotionElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimateTransformElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimateTransformElement-devel

This package contains library source intended for building other packages which
use the "SvgAnimateTransformElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimatedAngle-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimatedAngle-devel

This package contains library source intended for building other packages which
use the "SvgAnimatedAngle" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimatedBoolean-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimatedBoolean-devel

This package contains library source intended for building other packages which
use the "SvgAnimatedBoolean" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimatedEnumeration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimatedEnumeration-devel

This package contains library source intended for building other packages which
use the "SvgAnimatedEnumeration" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimatedInteger-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimatedInteger-devel

This package contains library source intended for building other packages which
use the "SvgAnimatedInteger" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimatedLength-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimatedLength-devel

This package contains library source intended for building other packages which
use the "SvgAnimatedLength" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimatedLengthList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimatedLengthList-devel

This package contains library source intended for building other packages which
use the "SvgAnimatedLengthList" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimatedNumber-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimatedNumber-devel

This package contains library source intended for building other packages which
use the "SvgAnimatedNumber" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimatedNumberList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimatedNumberList-devel

This package contains library source intended for building other packages which
use the "SvgAnimatedNumberList" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimatedPreserveAspectRatio-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimatedPreserveAspectRatio-devel

This package contains library source intended for building other packages which
use the "SvgAnimatedPreserveAspectRatio" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimatedRect-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimatedRect-devel

This package contains library source intended for building other packages which
use the "SvgAnimatedRect" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimatedString-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimatedString-devel

This package contains library source intended for building other packages which
use the "SvgAnimatedString" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimatedTransformList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimatedTransformList-devel

This package contains library source intended for building other packages which
use the "SvgAnimatedTransformList" feature of the "%{crate}" crate.

%package     -n %{name}+SvgAnimationElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgAnimationElement-devel

This package contains library source intended for building other packages which
use the "SvgAnimationElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgBoundingBoxOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgBoundingBoxOptions-devel

This package contains library source intended for building other packages which
use the "SvgBoundingBoxOptions" feature of the "%{crate}" crate.

%package     -n %{name}+SvgCircleElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgCircleElement-devel

This package contains library source intended for building other packages which
use the "SvgCircleElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgClipPathElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgClipPathElement-devel

This package contains library source intended for building other packages which
use the "SvgClipPathElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgComponentTransferFunctionElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgComponentTransferFunctionElement-devel

This package contains library source intended for building other packages which
use the "SvgComponentTransferFunctionElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgDefsElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgDefsElement-devel

This package contains library source intended for building other packages which
use the "SvgDefsElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgDescElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgDescElement-devel

This package contains library source intended for building other packages which
use the "SvgDescElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgElement-devel

This package contains library source intended for building other packages which
use the "SvgElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgEllipseElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgEllipseElement-devel

This package contains library source intended for building other packages which
use the "SvgEllipseElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgFilterElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgFilterElement-devel

This package contains library source intended for building other packages which
use the "SvgFilterElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgForeignObjectElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgForeignObjectElement-devel

This package contains library source intended for building other packages which
use the "SvgForeignObjectElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgGeometryElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgGeometryElement-devel

This package contains library source intended for building other packages which
use the "SvgGeometryElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgGradientElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgGradientElement-devel

This package contains library source intended for building other packages which
use the "SvgGradientElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgGraphicsElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgGraphicsElement-devel

This package contains library source intended for building other packages which
use the "SvgGraphicsElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgImageElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgImageElement-devel

This package contains library source intended for building other packages which
use the "SvgImageElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgLength-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgLength-devel

This package contains library source intended for building other packages which
use the "SvgLength" feature of the "%{crate}" crate.

%package     -n %{name}+SvgLengthList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgLengthList-devel

This package contains library source intended for building other packages which
use the "SvgLengthList" feature of the "%{crate}" crate.

%package     -n %{name}+SvgLineElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgLineElement-devel

This package contains library source intended for building other packages which
use the "SvgLineElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgLinearGradientElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgLinearGradientElement-devel

This package contains library source intended for building other packages which
use the "SvgLinearGradientElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgMarkerElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgMarkerElement-devel

This package contains library source intended for building other packages which
use the "SvgMarkerElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgMaskElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgMaskElement-devel

This package contains library source intended for building other packages which
use the "SvgMaskElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgMatrix-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgMatrix-devel

This package contains library source intended for building other packages which
use the "SvgMatrix" feature of the "%{crate}" crate.

%package     -n %{name}+SvgMetadataElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgMetadataElement-devel

This package contains library source intended for building other packages which
use the "SvgMetadataElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgNumber-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgNumber-devel

This package contains library source intended for building other packages which
use the "SvgNumber" feature of the "%{crate}" crate.

%package     -n %{name}+SvgNumberList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgNumberList-devel

This package contains library source intended for building other packages which
use the "SvgNumberList" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathElement-devel

This package contains library source intended for building other packages which
use the "SvgPathElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSeg-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSeg-devel

This package contains library source intended for building other packages which
use the "SvgPathSeg" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegArcAbs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegArcAbs-devel

This package contains library source intended for building other packages which
use the "SvgPathSegArcAbs" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegArcRel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegArcRel-devel

This package contains library source intended for building other packages which
use the "SvgPathSegArcRel" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegClosePath-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegClosePath-devel

This package contains library source intended for building other packages which
use the "SvgPathSegClosePath" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegCurvetoCubicAbs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegCurvetoCubicAbs-devel

This package contains library source intended for building other packages which
use the "SvgPathSegCurvetoCubicAbs" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegCurvetoCubicRel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegCurvetoCubicRel-devel

This package contains library source intended for building other packages which
use the "SvgPathSegCurvetoCubicRel" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegCurvetoCubicSmoothAbs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegCurvetoCubicSmoothAbs-devel

This package contains library source intended for building other packages which
use the "SvgPathSegCurvetoCubicSmoothAbs" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegCurvetoCubicSmoothRel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegCurvetoCubicSmoothRel-devel

This package contains library source intended for building other packages which
use the "SvgPathSegCurvetoCubicSmoothRel" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegCurvetoQuadraticAbs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegCurvetoQuadraticAbs-devel

This package contains library source intended for building other packages which
use the "SvgPathSegCurvetoQuadraticAbs" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegCurvetoQuadraticRel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegCurvetoQuadraticRel-devel

This package contains library source intended for building other packages which
use the "SvgPathSegCurvetoQuadraticRel" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegCurvetoQuadraticSmoothAbs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegCurvetoQuadraticSmoothAbs-devel

This package contains library source intended for building other packages which
use the "SvgPathSegCurvetoQuadraticSmoothAbs" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegCurvetoQuadraticSmoothRel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegCurvetoQuadraticSmoothRel-devel

This package contains library source intended for building other packages which
use the "SvgPathSegCurvetoQuadraticSmoothRel" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegLinetoAbs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegLinetoAbs-devel

This package contains library source intended for building other packages which
use the "SvgPathSegLinetoAbs" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegLinetoHorizontalAbs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegLinetoHorizontalAbs-devel

This package contains library source intended for building other packages which
use the "SvgPathSegLinetoHorizontalAbs" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegLinetoHorizontalRel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegLinetoHorizontalRel-devel

This package contains library source intended for building other packages which
use the "SvgPathSegLinetoHorizontalRel" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegLinetoRel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegLinetoRel-devel

This package contains library source intended for building other packages which
use the "SvgPathSegLinetoRel" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegLinetoVerticalAbs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegLinetoVerticalAbs-devel

This package contains library source intended for building other packages which
use the "SvgPathSegLinetoVerticalAbs" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegLinetoVerticalRel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegLinetoVerticalRel-devel

This package contains library source intended for building other packages which
use the "SvgPathSegLinetoVerticalRel" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegList-devel

This package contains library source intended for building other packages which
use the "SvgPathSegList" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegMovetoAbs-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegMovetoAbs-devel

This package contains library source intended for building other packages which
use the "SvgPathSegMovetoAbs" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPathSegMovetoRel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPathSegMovetoRel-devel

This package contains library source intended for building other packages which
use the "SvgPathSegMovetoRel" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPatternElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPatternElement-devel

This package contains library source intended for building other packages which
use the "SvgPatternElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPoint-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPoint-devel

This package contains library source intended for building other packages which
use the "SvgPoint" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPointList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPointList-devel

This package contains library source intended for building other packages which
use the "SvgPointList" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPolygonElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPolygonElement-devel

This package contains library source intended for building other packages which
use the "SvgPolygonElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPolylineElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPolylineElement-devel

This package contains library source intended for building other packages which
use the "SvgPolylineElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgPreserveAspectRatio-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgPreserveAspectRatio-devel

This package contains library source intended for building other packages which
use the "SvgPreserveAspectRatio" feature of the "%{crate}" crate.

%package     -n %{name}+SvgRadialGradientElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgRadialGradientElement-devel

This package contains library source intended for building other packages which
use the "SvgRadialGradientElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgRect-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgRect-devel

This package contains library source intended for building other packages which
use the "SvgRect" feature of the "%{crate}" crate.

%package     -n %{name}+SvgRectElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgRectElement-devel

This package contains library source intended for building other packages which
use the "SvgRectElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgScriptElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgScriptElement-devel

This package contains library source intended for building other packages which
use the "SvgScriptElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgSetElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgSetElement-devel

This package contains library source intended for building other packages which
use the "SvgSetElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgStopElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgStopElement-devel

This package contains library source intended for building other packages which
use the "SvgStopElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgStringList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgStringList-devel

This package contains library source intended for building other packages which
use the "SvgStringList" feature of the "%{crate}" crate.

%package     -n %{name}+SvgStyleElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgStyleElement-devel

This package contains library source intended for building other packages which
use the "SvgStyleElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgSwitchElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgSwitchElement-devel

This package contains library source intended for building other packages which
use the "SvgSwitchElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgSymbolElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgSymbolElement-devel

This package contains library source intended for building other packages which
use the "SvgSymbolElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgTextContentElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgTextContentElement-devel

This package contains library source intended for building other packages which
use the "SvgTextContentElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgTextElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgTextElement-devel

This package contains library source intended for building other packages which
use the "SvgTextElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgTextPathElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgTextPathElement-devel

This package contains library source intended for building other packages which
use the "SvgTextPathElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgTextPositioningElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgTextPositioningElement-devel

This package contains library source intended for building other packages which
use the "SvgTextPositioningElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgTitleElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgTitleElement-devel

This package contains library source intended for building other packages which
use the "SvgTitleElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgTransform-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgTransform-devel

This package contains library source intended for building other packages which
use the "SvgTransform" feature of the "%{crate}" crate.

%package     -n %{name}+SvgTransformList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgTransformList-devel

This package contains library source intended for building other packages which
use the "SvgTransformList" feature of the "%{crate}" crate.

%package     -n %{name}+SvgUnitTypes-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgUnitTypes-devel

This package contains library source intended for building other packages which
use the "SvgUnitTypes" feature of the "%{crate}" crate.

%package     -n %{name}+SvgUseElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgUseElement-devel

This package contains library source intended for building other packages which
use the "SvgUseElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgViewElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgViewElement-devel

This package contains library source intended for building other packages which
use the "SvgViewElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgZoomAndPan-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgZoomAndPan-devel

This package contains library source intended for building other packages which
use the "SvgZoomAndPan" feature of the "%{crate}" crate.

%package     -n %{name}+SvgaElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgaElement-devel

This package contains library source intended for building other packages which
use the "SvgaElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeBlendElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeBlendElement-devel

This package contains library source intended for building other packages which
use the "SvgfeBlendElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeColorMatrixElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeColorMatrixElement-devel

This package contains library source intended for building other packages which
use the "SvgfeColorMatrixElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeComponentTransferElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeComponentTransferElement-devel

This package contains library source intended for building other packages which
use the "SvgfeComponentTransferElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeCompositeElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeCompositeElement-devel

This package contains library source intended for building other packages which
use the "SvgfeCompositeElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeConvolveMatrixElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeConvolveMatrixElement-devel

This package contains library source intended for building other packages which
use the "SvgfeConvolveMatrixElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeDiffuseLightingElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeDiffuseLightingElement-devel

This package contains library source intended for building other packages which
use the "SvgfeDiffuseLightingElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeDisplacementMapElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeDisplacementMapElement-devel

This package contains library source intended for building other packages which
use the "SvgfeDisplacementMapElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeDistantLightElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeDistantLightElement-devel

This package contains library source intended for building other packages which
use the "SvgfeDistantLightElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeDropShadowElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeDropShadowElement-devel

This package contains library source intended for building other packages which
use the "SvgfeDropShadowElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeFloodElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeFloodElement-devel

This package contains library source intended for building other packages which
use the "SvgfeFloodElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeFuncAElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeFuncAElement-devel

This package contains library source intended for building other packages which
use the "SvgfeFuncAElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeFuncBElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeFuncBElement-devel

This package contains library source intended for building other packages which
use the "SvgfeFuncBElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeFuncGElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeFuncGElement-devel

This package contains library source intended for building other packages which
use the "SvgfeFuncGElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeFuncRElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeFuncRElement-devel

This package contains library source intended for building other packages which
use the "SvgfeFuncRElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeGaussianBlurElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeGaussianBlurElement-devel

This package contains library source intended for building other packages which
use the "SvgfeGaussianBlurElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeImageElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeImageElement-devel

This package contains library source intended for building other packages which
use the "SvgfeImageElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeMergeElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeMergeElement-devel

This package contains library source intended for building other packages which
use the "SvgfeMergeElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeMergeNodeElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeMergeNodeElement-devel

This package contains library source intended for building other packages which
use the "SvgfeMergeNodeElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeMorphologyElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeMorphologyElement-devel

This package contains library source intended for building other packages which
use the "SvgfeMorphologyElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeOffsetElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeOffsetElement-devel

This package contains library source intended for building other packages which
use the "SvgfeOffsetElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfePointLightElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfePointLightElement-devel

This package contains library source intended for building other packages which
use the "SvgfePointLightElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeSpecularLightingElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeSpecularLightingElement-devel

This package contains library source intended for building other packages which
use the "SvgfeSpecularLightingElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeSpotLightElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeSpotLightElement-devel

This package contains library source intended for building other packages which
use the "SvgfeSpotLightElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeTileElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeTileElement-devel

This package contains library source intended for building other packages which
use the "SvgfeTileElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgfeTurbulenceElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgfeTurbulenceElement-devel

This package contains library source intended for building other packages which
use the "SvgfeTurbulenceElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvggElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvggElement-devel

This package contains library source intended for building other packages which
use the "SvggElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgmPathElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgmPathElement-devel

This package contains library source intended for building other packages which
use the "SvgmPathElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgsvgElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgsvgElement-devel

This package contains library source intended for building other packages which
use the "SvgsvgElement" feature of the "%{crate}" crate.

%package     -n %{name}+SvgtSpanElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+SvgtSpanElement-devel

This package contains library source intended for building other packages which
use the "SvgtSpanElement" feature of the "%{crate}" crate.

%package     -n %{name}+TaskController-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TaskController-devel

This package contains library source intended for building other packages which
use the "TaskController" feature of the "%{crate}" crate.

%package     -n %{name}+TaskControllerInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TaskControllerInit-devel

This package contains library source intended for building other packages which
use the "TaskControllerInit" feature of the "%{crate}" crate.

%package     -n %{name}+TaskPriority-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TaskPriority-devel

This package contains library source intended for building other packages which
use the "TaskPriority" feature of the "%{crate}" crate.

%package     -n %{name}+TaskPriorityChangeEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TaskPriorityChangeEvent-devel

This package contains library source intended for building other packages which
use the "TaskPriorityChangeEvent" feature of the "%{crate}" crate.

%package     -n %{name}+TaskPriorityChangeEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TaskPriorityChangeEventInit-devel

This package contains library source intended for building other packages which
use the "TaskPriorityChangeEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+TaskSignal-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TaskSignal-devel

This package contains library source intended for building other packages which
use the "TaskSignal" feature of the "%{crate}" crate.

%package     -n %{name}+TaskSignalAnyInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TaskSignalAnyInit-devel

This package contains library source intended for building other packages which
use the "TaskSignalAnyInit" feature of the "%{crate}" crate.

%package     -n %{name}+TcpReadyState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TcpReadyState-devel

This package contains library source intended for building other packages which
use the "TcpReadyState" feature of the "%{crate}" crate.

%package     -n %{name}+TcpServerSocket-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TcpServerSocket-devel

This package contains library source intended for building other packages which
use the "TcpServerSocket" feature of the "%{crate}" crate.

%package     -n %{name}+TcpServerSocketEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TcpServerSocketEvent-devel

This package contains library source intended for building other packages which
use the "TcpServerSocketEvent" feature of the "%{crate}" crate.

%package     -n %{name}+TcpServerSocketEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TcpServerSocketEventInit-devel

This package contains library source intended for building other packages which
use the "TcpServerSocketEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+TcpSocket-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TcpSocket-devel

This package contains library source intended for building other packages which
use the "TcpSocket" feature of the "%{crate}" crate.

%package     -n %{name}+TcpSocketBinaryType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TcpSocketBinaryType-devel

This package contains library source intended for building other packages which
use the "TcpSocketBinaryType" feature of the "%{crate}" crate.

%package     -n %{name}+TcpSocketErrorEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TcpSocketErrorEvent-devel

This package contains library source intended for building other packages which
use the "TcpSocketErrorEvent" feature of the "%{crate}" crate.

%package     -n %{name}+TcpSocketErrorEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TcpSocketErrorEventInit-devel

This package contains library source intended for building other packages which
use the "TcpSocketErrorEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+TcpSocketEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TcpSocketEvent-devel

This package contains library source intended for building other packages which
use the "TcpSocketEvent" feature of the "%{crate}" crate.

%package     -n %{name}+TcpSocketEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TcpSocketEventInit-devel

This package contains library source intended for building other packages which
use the "TcpSocketEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+Text-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Text-devel

This package contains library source intended for building other packages which
use the "Text" feature of the "%{crate}" crate.

%package     -n %{name}+TextDecodeOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TextDecodeOptions-devel

This package contains library source intended for building other packages which
use the "TextDecodeOptions" feature of the "%{crate}" crate.

%package     -n %{name}+TextDecoder-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TextDecoder-devel

This package contains library source intended for building other packages which
use the "TextDecoder" feature of the "%{crate}" crate.

%package     -n %{name}+TextDecoderOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TextDecoderOptions-devel

This package contains library source intended for building other packages which
use the "TextDecoderOptions" feature of the "%{crate}" crate.

%package     -n %{name}+TextEncoder-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TextEncoder-devel

This package contains library source intended for building other packages which
use the "TextEncoder" feature of the "%{crate}" crate.

%package     -n %{name}+TextMetrics-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TextMetrics-devel

This package contains library source intended for building other packages which
use the "TextMetrics" feature of the "%{crate}" crate.

%package     -n %{name}+TextTrack-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TextTrack-devel

This package contains library source intended for building other packages which
use the "TextTrack" feature of the "%{crate}" crate.

%package     -n %{name}+TextTrackCue-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TextTrackCue-devel

This package contains library source intended for building other packages which
use the "TextTrackCue" feature of the "%{crate}" crate.

%package     -n %{name}+TextTrackCueList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TextTrackCueList-devel

This package contains library source intended for building other packages which
use the "TextTrackCueList" feature of the "%{crate}" crate.

%package     -n %{name}+TextTrackKind-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TextTrackKind-devel

This package contains library source intended for building other packages which
use the "TextTrackKind" feature of the "%{crate}" crate.

%package     -n %{name}+TextTrackList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TextTrackList-devel

This package contains library source intended for building other packages which
use the "TextTrackList" feature of the "%{crate}" crate.

%package     -n %{name}+TextTrackMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TextTrackMode-devel

This package contains library source intended for building other packages which
use the "TextTrackMode" feature of the "%{crate}" crate.

%package     -n %{name}+TimeEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TimeEvent-devel

This package contains library source intended for building other packages which
use the "TimeEvent" feature of the "%{crate}" crate.

%package     -n %{name}+TimeRanges-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TimeRanges-devel

This package contains library source intended for building other packages which
use the "TimeRanges" feature of the "%{crate}" crate.

%package     -n %{name}+ToggleEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ToggleEvent-devel

This package contains library source intended for building other packages which
use the "ToggleEvent" feature of the "%{crate}" crate.

%package     -n %{name}+ToggleEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ToggleEventInit-devel

This package contains library source intended for building other packages which
use the "ToggleEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+TogglePopoverOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TogglePopoverOptions-devel

This package contains library source intended for building other packages which
use the "TogglePopoverOptions" feature of the "%{crate}" crate.

%package     -n %{name}+TokenBinding-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TokenBinding-devel

This package contains library source intended for building other packages which
use the "TokenBinding" feature of the "%{crate}" crate.

%package     -n %{name}+TokenBindingStatus-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TokenBindingStatus-devel

This package contains library source intended for building other packages which
use the "TokenBindingStatus" feature of the "%{crate}" crate.

%package     -n %{name}+Touch-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Touch-devel

This package contains library source intended for building other packages which
use the "Touch" feature of the "%{crate}" crate.

%package     -n %{name}+TouchEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TouchEvent-devel

This package contains library source intended for building other packages which
use the "TouchEvent" feature of the "%{crate}" crate.

%package     -n %{name}+TouchEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TouchEventInit-devel

This package contains library source intended for building other packages which
use the "TouchEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+TouchInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TouchInit-devel

This package contains library source intended for building other packages which
use the "TouchInit" feature of the "%{crate}" crate.

%package     -n %{name}+TouchList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TouchList-devel

This package contains library source intended for building other packages which
use the "TouchList" feature of the "%{crate}" crate.

%package     -n %{name}+TrackEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TrackEvent-devel

This package contains library source intended for building other packages which
use the "TrackEvent" feature of the "%{crate}" crate.

%package     -n %{name}+TrackEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TrackEventInit-devel

This package contains library source intended for building other packages which
use the "TrackEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+TransformStream-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TransformStream-devel

This package contains library source intended for building other packages which
use the "TransformStream" feature of the "%{crate}" crate.

%package     -n %{name}+TransformStreamDefaultController-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TransformStreamDefaultController-devel

This package contains library source intended for building other packages which
use the "TransformStreamDefaultController" feature of the "%{crate}" crate.

%package     -n %{name}+Transformer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Transformer-devel

This package contains library source intended for building other packages which
use the "Transformer" feature of the "%{crate}" crate.

%package     -n %{name}+TransitionEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TransitionEvent-devel

This package contains library source intended for building other packages which
use the "TransitionEvent" feature of the "%{crate}" crate.

%package     -n %{name}+TransitionEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TransitionEventInit-devel

This package contains library source intended for building other packages which
use the "TransitionEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+Transport-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Transport-devel

This package contains library source intended for building other packages which
use the "Transport" feature of the "%{crate}" crate.

%package     -n %{name}+TreeBoxObject-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TreeBoxObject-devel

This package contains library source intended for building other packages which
use the "TreeBoxObject" feature of the "%{crate}" crate.

%package     -n %{name}+TreeCellInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TreeCellInfo-devel

This package contains library source intended for building other packages which
use the "TreeCellInfo" feature of the "%{crate}" crate.

%package     -n %{name}+TreeView-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TreeView-devel

This package contains library source intended for building other packages which
use the "TreeView" feature of the "%{crate}" crate.

%package     -n %{name}+TreeWalker-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+TreeWalker-devel

This package contains library source intended for building other packages which
use the "TreeWalker" feature of the "%{crate}" crate.

%package     -n %{name}+U2f-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+U2f-devel

This package contains library source intended for building other packages which
use the "U2f" feature of the "%{crate}" crate.

%package     -n %{name}+U2fClientData-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+U2fClientData-devel

This package contains library source intended for building other packages which
use the "U2fClientData" feature of the "%{crate}" crate.

%package     -n %{name}+ULongRange-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ULongRange-devel

This package contains library source intended for building other packages which
use the "ULongRange" feature of the "%{crate}" crate.

%package     -n %{name}+UaDataValues-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UaDataValues-devel

This package contains library source intended for building other packages which
use the "UaDataValues" feature of the "%{crate}" crate.

%package     -n %{name}+UaLowEntropyJson-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UaLowEntropyJson-devel

This package contains library source intended for building other packages which
use the "UaLowEntropyJson" feature of the "%{crate}" crate.

%package     -n %{name}+UdpMessageEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UdpMessageEventInit-devel

This package contains library source intended for building other packages which
use the "UdpMessageEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+UdpOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UdpOptions-devel

This package contains library source intended for building other packages which
use the "UdpOptions" feature of the "%{crate}" crate.

%package     -n %{name}+UiEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UiEvent-devel

This package contains library source intended for building other packages which
use the "UiEvent" feature of the "%{crate}" crate.

%package     -n %{name}+UiEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UiEventInit-devel

This package contains library source intended for building other packages which
use the "UiEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+UnderlyingSink-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UnderlyingSink-devel

This package contains library source intended for building other packages which
use the "UnderlyingSink" feature of the "%{crate}" crate.

%package     -n %{name}+UnderlyingSource-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UnderlyingSource-devel

This package contains library source intended for building other packages which
use the "UnderlyingSource" feature of the "%{crate}" crate.

%package     -n %{name}+Url-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Url-devel

This package contains library source intended for building other packages which
use the "Url" feature of the "%{crate}" crate.

%package     -n %{name}+UrlSearchParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UrlSearchParams-devel

This package contains library source intended for building other packages which
use the "UrlSearchParams" feature of the "%{crate}" crate.

%package     -n %{name}+Usb-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Usb-devel

This package contains library source intended for building other packages which
use the "Usb" feature of the "%{crate}" crate.

%package     -n %{name}+UsbAlternateInterface-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbAlternateInterface-devel

This package contains library source intended for building other packages which
use the "UsbAlternateInterface" feature of the "%{crate}" crate.

%package     -n %{name}+UsbConfiguration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbConfiguration-devel

This package contains library source intended for building other packages which
use the "UsbConfiguration" feature of the "%{crate}" crate.

%package     -n %{name}+UsbConnectionEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbConnectionEvent-devel

This package contains library source intended for building other packages which
use the "UsbConnectionEvent" feature of the "%{crate}" crate.

%package     -n %{name}+UsbConnectionEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbConnectionEventInit-devel

This package contains library source intended for building other packages which
use the "UsbConnectionEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+UsbControlTransferParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbControlTransferParameters-devel

This package contains library source intended for building other packages which
use the "UsbControlTransferParameters" feature of the "%{crate}" crate.

%package     -n %{name}+UsbDevice-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbDevice-devel

This package contains library source intended for building other packages which
use the "UsbDevice" feature of the "%{crate}" crate.

%package     -n %{name}+UsbDeviceFilter-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbDeviceFilter-devel

This package contains library source intended for building other packages which
use the "UsbDeviceFilter" feature of the "%{crate}" crate.

%package     -n %{name}+UsbDeviceRequestOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbDeviceRequestOptions-devel

This package contains library source intended for building other packages which
use the "UsbDeviceRequestOptions" feature of the "%{crate}" crate.

%package     -n %{name}+UsbDirection-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbDirection-devel

This package contains library source intended for building other packages which
use the "UsbDirection" feature of the "%{crate}" crate.

%package     -n %{name}+UsbEndpoint-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbEndpoint-devel

This package contains library source intended for building other packages which
use the "UsbEndpoint" feature of the "%{crate}" crate.

%package     -n %{name}+UsbEndpointType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbEndpointType-devel

This package contains library source intended for building other packages which
use the "UsbEndpointType" feature of the "%{crate}" crate.

%package     -n %{name}+UsbInTransferResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbInTransferResult-devel

This package contains library source intended for building other packages which
use the "UsbInTransferResult" feature of the "%{crate}" crate.

%package     -n %{name}+UsbInterface-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbInterface-devel

This package contains library source intended for building other packages which
use the "UsbInterface" feature of the "%{crate}" crate.

%package     -n %{name}+UsbIsochronousInTransferPacket-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbIsochronousInTransferPacket-devel

This package contains library source intended for building other packages which
use the "UsbIsochronousInTransferPacket" feature of the "%{crate}" crate.

%package     -n %{name}+UsbIsochronousInTransferResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbIsochronousInTransferResult-devel

This package contains library source intended for building other packages which
use the "UsbIsochronousInTransferResult" feature of the "%{crate}" crate.

%package     -n %{name}+UsbIsochronousOutTransferPacket-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbIsochronousOutTransferPacket-devel

This package contains library source intended for building other packages which
use the "UsbIsochronousOutTransferPacket" feature of the "%{crate}" crate.

%package     -n %{name}+UsbIsochronousOutTransferResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbIsochronousOutTransferResult-devel

This package contains library source intended for building other packages which
use the "UsbIsochronousOutTransferResult" feature of the "%{crate}" crate.

%package     -n %{name}+UsbOutTransferResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbOutTransferResult-devel

This package contains library source intended for building other packages which
use the "UsbOutTransferResult" feature of the "%{crate}" crate.

%package     -n %{name}+UsbPermissionDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbPermissionDescriptor-devel

This package contains library source intended for building other packages which
use the "UsbPermissionDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+UsbPermissionResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbPermissionResult-devel

This package contains library source intended for building other packages which
use the "UsbPermissionResult" feature of the "%{crate}" crate.

%package     -n %{name}+UsbPermissionStorage-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbPermissionStorage-devel

This package contains library source intended for building other packages which
use the "UsbPermissionStorage" feature of the "%{crate}" crate.

%package     -n %{name}+UsbRecipient-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbRecipient-devel

This package contains library source intended for building other packages which
use the "UsbRecipient" feature of the "%{crate}" crate.

%package     -n %{name}+UsbRequestType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbRequestType-devel

This package contains library source intended for building other packages which
use the "UsbRequestType" feature of the "%{crate}" crate.

%package     -n %{name}+UsbTransferStatus-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UsbTransferStatus-devel

This package contains library source intended for building other packages which
use the "UsbTransferStatus" feature of the "%{crate}" crate.

%package     -n %{name}+UserActivation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UserActivation-devel

This package contains library source intended for building other packages which
use the "UserActivation" feature of the "%{crate}" crate.

%package     -n %{name}+UserProximityEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UserProximityEvent-devel

This package contains library source intended for building other packages which
use the "UserProximityEvent" feature of the "%{crate}" crate.

%package     -n %{name}+UserProximityEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UserProximityEventInit-devel

This package contains library source intended for building other packages which
use the "UserProximityEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+UserVerificationRequirement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+UserVerificationRequirement-devel

This package contains library source intended for building other packages which
use the "UserVerificationRequirement" feature of the "%{crate}" crate.

%package     -n %{name}+ValidityState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ValidityState-devel

This package contains library source intended for building other packages which
use the "ValidityState" feature of the "%{crate}" crate.

%package     -n %{name}+ValueEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ValueEvent-devel

This package contains library source intended for building other packages which
use the "ValueEvent" feature of the "%{crate}" crate.

%package     -n %{name}+ValueEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ValueEventInit-devel

This package contains library source intended for building other packages which
use the "ValueEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+VideoColorPrimaries-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoColorPrimaries-devel

This package contains library source intended for building other packages which
use the "VideoColorPrimaries" feature of the "%{crate}" crate.

%package     -n %{name}+VideoColorSpace-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoColorSpace-devel

This package contains library source intended for building other packages which
use the "VideoColorSpace" feature of the "%{crate}" crate.

%package     -n %{name}+VideoColorSpaceInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoColorSpaceInit-devel

This package contains library source intended for building other packages which
use the "VideoColorSpaceInit" feature of the "%{crate}" crate.

%package     -n %{name}+VideoConfiguration-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoConfiguration-devel

This package contains library source intended for building other packages which
use the "VideoConfiguration" feature of the "%{crate}" crate.

%package     -n %{name}+VideoDecoder-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoDecoder-devel

This package contains library source intended for building other packages which
use the "VideoDecoder" feature of the "%{crate}" crate.

%package     -n %{name}+VideoDecoderConfig-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoDecoderConfig-devel

This package contains library source intended for building other packages which
use the "VideoDecoderConfig" feature of the "%{crate}" crate.

%package     -n %{name}+VideoDecoderInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoDecoderInit-devel

This package contains library source intended for building other packages which
use the "VideoDecoderInit" feature of the "%{crate}" crate.

%package     -n %{name}+VideoDecoderSupport-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoDecoderSupport-devel

This package contains library source intended for building other packages which
use the "VideoDecoderSupport" feature of the "%{crate}" crate.

%package     -n %{name}+VideoEncoder-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoEncoder-devel

This package contains library source intended for building other packages which
use the "VideoEncoder" feature of the "%{crate}" crate.

%package     -n %{name}+VideoEncoderBitrateMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoEncoderBitrateMode-devel

This package contains library source intended for building other packages which
use the "VideoEncoderBitrateMode" feature of the "%{crate}" crate.

%package     -n %{name}+VideoEncoderConfig-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoEncoderConfig-devel

This package contains library source intended for building other packages which
use the "VideoEncoderConfig" feature of the "%{crate}" crate.

%package     -n %{name}+VideoEncoderEncodeOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoEncoderEncodeOptions-devel

This package contains library source intended for building other packages which
use the "VideoEncoderEncodeOptions" feature of the "%{crate}" crate.

%package     -n %{name}+VideoEncoderInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoEncoderInit-devel

This package contains library source intended for building other packages which
use the "VideoEncoderInit" feature of the "%{crate}" crate.

%package     -n %{name}+VideoEncoderSupport-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoEncoderSupport-devel

This package contains library source intended for building other packages which
use the "VideoEncoderSupport" feature of the "%{crate}" crate.

%package     -n %{name}+VideoFacingModeEnum-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoFacingModeEnum-devel

This package contains library source intended for building other packages which
use the "VideoFacingModeEnum" feature of the "%{crate}" crate.

%package     -n %{name}+VideoFrame-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoFrame-devel

This package contains library source intended for building other packages which
use the "VideoFrame" feature of the "%{crate}" crate.

%package     -n %{name}+VideoFrameBufferInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoFrameBufferInit-devel

This package contains library source intended for building other packages which
use the "VideoFrameBufferInit" feature of the "%{crate}" crate.

%package     -n %{name}+VideoFrameCopyToOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoFrameCopyToOptions-devel

This package contains library source intended for building other packages which
use the "VideoFrameCopyToOptions" feature of the "%{crate}" crate.

%package     -n %{name}+VideoFrameInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoFrameInit-devel

This package contains library source intended for building other packages which
use the "VideoFrameInit" feature of the "%{crate}" crate.

%package     -n %{name}+VideoFrameMetadata-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoFrameMetadata-devel

This package contains library source intended for building other packages which
use the "VideoFrameMetadata" feature of the "%{crate}" crate.

%package     -n %{name}+VideoMatrixCoefficients-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoMatrixCoefficients-devel

This package contains library source intended for building other packages which
use the "VideoMatrixCoefficients" feature of the "%{crate}" crate.

%package     -n %{name}+VideoPixelFormat-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoPixelFormat-devel

This package contains library source intended for building other packages which
use the "VideoPixelFormat" feature of the "%{crate}" crate.

%package     -n %{name}+VideoPlaybackQuality-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoPlaybackQuality-devel

This package contains library source intended for building other packages which
use the "VideoPlaybackQuality" feature of the "%{crate}" crate.

%package     -n %{name}+VideoStreamTrack-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoStreamTrack-devel

This package contains library source intended for building other packages which
use the "VideoStreamTrack" feature of the "%{crate}" crate.

%package     -n %{name}+VideoTrack-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoTrack-devel

This package contains library source intended for building other packages which
use the "VideoTrack" feature of the "%{crate}" crate.

%package     -n %{name}+VideoTrackList-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoTrackList-devel

This package contains library source intended for building other packages which
use the "VideoTrackList" feature of the "%{crate}" crate.

%package     -n %{name}+VideoTransferCharacteristics-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VideoTransferCharacteristics-devel

This package contains library source intended for building other packages which
use the "VideoTransferCharacteristics" feature of the "%{crate}" crate.

%package     -n %{name}+ViewTransition-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ViewTransition-devel

This package contains library source intended for building other packages which
use the "ViewTransition" feature of the "%{crate}" crate.

%package     -n %{name}+ViewTransitionTypeSet-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+ViewTransitionTypeSet-devel

This package contains library source intended for building other packages which
use the "ViewTransitionTypeSet" feature of the "%{crate}" crate.

%package     -n %{name}+VisibilityState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VisibilityState-devel

This package contains library source intended for building other packages which
use the "VisibilityState" feature of the "%{crate}" crate.

%package     -n %{name}+VisualViewport-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VisualViewport-devel

This package contains library source intended for building other packages which
use the "VisualViewport" feature of the "%{crate}" crate.

%package     -n %{name}+VoidCallback-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VoidCallback-devel

This package contains library source intended for building other packages which
use the "VoidCallback" feature of the "%{crate}" crate.

%package     -n %{name}+VrDisplay-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VrDisplay-devel

This package contains library source intended for building other packages which
use the "VrDisplay" feature of the "%{crate}" crate.

%package     -n %{name}+VrDisplayCapabilities-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VrDisplayCapabilities-devel

This package contains library source intended for building other packages which
use the "VrDisplayCapabilities" feature of the "%{crate}" crate.

%package     -n %{name}+VrEye-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VrEye-devel

This package contains library source intended for building other packages which
use the "VrEye" feature of the "%{crate}" crate.

%package     -n %{name}+VrEyeParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VrEyeParameters-devel

This package contains library source intended for building other packages which
use the "VrEyeParameters" feature of the "%{crate}" crate.

%package     -n %{name}+VrFieldOfView-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VrFieldOfView-devel

This package contains library source intended for building other packages which
use the "VrFieldOfView" feature of the "%{crate}" crate.

%package     -n %{name}+VrFrameData-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VrFrameData-devel

This package contains library source intended for building other packages which
use the "VrFrameData" feature of the "%{crate}" crate.

%package     -n %{name}+VrLayer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VrLayer-devel

This package contains library source intended for building other packages which
use the "VrLayer" feature of the "%{crate}" crate.

%package     -n %{name}+VrMockController-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VrMockController-devel

This package contains library source intended for building other packages which
use the "VrMockController" feature of the "%{crate}" crate.

%package     -n %{name}+VrMockDisplay-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VrMockDisplay-devel

This package contains library source intended for building other packages which
use the "VrMockDisplay" feature of the "%{crate}" crate.

%package     -n %{name}+VrPose-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VrPose-devel

This package contains library source intended for building other packages which
use the "VrPose" feature of the "%{crate}" crate.

%package     -n %{name}+VrServiceTest-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VrServiceTest-devel

This package contains library source intended for building other packages which
use the "VrServiceTest" feature of the "%{crate}" crate.

%package     -n %{name}+VrStageParameters-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VrStageParameters-devel

This package contains library source intended for building other packages which
use the "VrStageParameters" feature of the "%{crate}" crate.

%package     -n %{name}+VrSubmitFrameResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VrSubmitFrameResult-devel

This package contains library source intended for building other packages which
use the "VrSubmitFrameResult" feature of the "%{crate}" crate.

%package     -n %{name}+VttCue-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VttCue-devel

This package contains library source intended for building other packages which
use the "VttCue" feature of the "%{crate}" crate.

%package     -n %{name}+VttRegion-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+VttRegion-devel

This package contains library source intended for building other packages which
use the "VttRegion" feature of the "%{crate}" crate.

%package     -n %{name}+WakeLock-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WakeLock-devel

This package contains library source intended for building other packages which
use the "WakeLock" feature of the "%{crate}" crate.

%package     -n %{name}+WakeLockSentinel-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WakeLockSentinel-devel

This package contains library source intended for building other packages which
use the "WakeLockSentinel" feature of the "%{crate}" crate.

%package     -n %{name}+WakeLockType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WakeLockType-devel

This package contains library source intended for building other packages which
use the "WakeLockType" feature of the "%{crate}" crate.

%package     -n %{name}+WatchAdvertisementsOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WatchAdvertisementsOptions-devel

This package contains library source intended for building other packages which
use the "WatchAdvertisementsOptions" feature of the "%{crate}" crate.

%package     -n %{name}+WaveShaperNode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WaveShaperNode-devel

This package contains library source intended for building other packages which
use the "WaveShaperNode" feature of the "%{crate}" crate.

%package     -n %{name}+WaveShaperOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WaveShaperOptions-devel

This package contains library source intended for building other packages which
use the "WaveShaperOptions" feature of the "%{crate}" crate.

%package     -n %{name}+WebGl2RenderingContext-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGl2RenderingContext-devel

This package contains library source intended for building other packages which
use the "WebGl2RenderingContext" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlActiveInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlActiveInfo-devel

This package contains library source intended for building other packages which
use the "WebGlActiveInfo" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlBuffer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlBuffer-devel

This package contains library source intended for building other packages which
use the "WebGlBuffer" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlContextAttributes-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlContextAttributes-devel

This package contains library source intended for building other packages which
use the "WebGlContextAttributes" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlContextEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlContextEvent-devel

This package contains library source intended for building other packages which
use the "WebGlContextEvent" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlContextEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlContextEventInit-devel

This package contains library source intended for building other packages which
use the "WebGlContextEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlFramebuffer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlFramebuffer-devel

This package contains library source intended for building other packages which
use the "WebGlFramebuffer" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlPowerPreference-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlPowerPreference-devel

This package contains library source intended for building other packages which
use the "WebGlPowerPreference" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlProgram-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlProgram-devel

This package contains library source intended for building other packages which
use the "WebGlProgram" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlQuery-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlQuery-devel

This package contains library source intended for building other packages which
use the "WebGlQuery" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlRenderbuffer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlRenderbuffer-devel

This package contains library source intended for building other packages which
use the "WebGlRenderbuffer" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlRenderingContext-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlRenderingContext-devel

This package contains library source intended for building other packages which
use the "WebGlRenderingContext" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlSampler-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlSampler-devel

This package contains library source intended for building other packages which
use the "WebGlSampler" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlShader-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlShader-devel

This package contains library source intended for building other packages which
use the "WebGlShader" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlShaderPrecisionFormat-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlShaderPrecisionFormat-devel

This package contains library source intended for building other packages which
use the "WebGlShaderPrecisionFormat" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlSync-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlSync-devel

This package contains library source intended for building other packages which
use the "WebGlSync" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlTexture-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlTexture-devel

This package contains library source intended for building other packages which
use the "WebGlTexture" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlTransformFeedback-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlTransformFeedback-devel

This package contains library source intended for building other packages which
use the "WebGlTransformFeedback" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlUniformLocation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlUniformLocation-devel

This package contains library source intended for building other packages which
use the "WebGlUniformLocation" feature of the "%{crate}" crate.

%package     -n %{name}+WebGlVertexArrayObject-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebGlVertexArrayObject-devel

This package contains library source intended for building other packages which
use the "WebGlVertexArrayObject" feature of the "%{crate}" crate.

%package     -n %{name}+WebKitCssMatrix-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebKitCssMatrix-devel

This package contains library source intended for building other packages which
use the "WebKitCssMatrix" feature of the "%{crate}" crate.

%package     -n %{name}+WebSocket-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebSocket-devel

This package contains library source intended for building other packages which
use the "WebSocket" feature of the "%{crate}" crate.

%package     -n %{name}+WebSocketDict-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebSocketDict-devel

This package contains library source intended for building other packages which
use the "WebSocketDict" feature of the "%{crate}" crate.

%package     -n %{name}+WebSocketElement-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebSocketElement-devel

This package contains library source intended for building other packages which
use the "WebSocketElement" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransport-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransport-devel

This package contains library source intended for building other packages which
use the "WebTransport" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportBidirectionalStream-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportBidirectionalStream-devel

This package contains library source intended for building other packages which
use the "WebTransportBidirectionalStream" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportCloseInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportCloseInfo-devel

This package contains library source intended for building other packages which
use the "WebTransportCloseInfo" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportCongestionControl-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportCongestionControl-devel

This package contains library source intended for building other packages which
use the "WebTransportCongestionControl" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportDatagramDuplexStream-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportDatagramDuplexStream-devel

This package contains library source intended for building other packages which
use the "WebTransportDatagramDuplexStream" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportDatagramStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportDatagramStats-devel

This package contains library source intended for building other packages which
use the "WebTransportDatagramStats" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportError-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportError-devel

This package contains library source intended for building other packages which
use the "WebTransportError" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportErrorOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportErrorOptions-devel

This package contains library source intended for building other packages which
use the "WebTransportErrorOptions" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportErrorSource-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportErrorSource-devel

This package contains library source intended for building other packages which
use the "WebTransportErrorSource" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportHash-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportHash-devel

This package contains library source intended for building other packages which
use the "WebTransportHash" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportOptions-devel

This package contains library source intended for building other packages which
use the "WebTransportOptions" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportReceiveStream-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportReceiveStream-devel

This package contains library source intended for building other packages which
use the "WebTransportReceiveStream" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportReceiveStreamStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportReceiveStreamStats-devel

This package contains library source intended for building other packages which
use the "WebTransportReceiveStreamStats" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportReliabilityMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportReliabilityMode-devel

This package contains library source intended for building other packages which
use the "WebTransportReliabilityMode" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportSendStream-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportSendStream-devel

This package contains library source intended for building other packages which
use the "WebTransportSendStream" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportSendStreamOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportSendStreamOptions-devel

This package contains library source intended for building other packages which
use the "WebTransportSendStreamOptions" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportSendStreamStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportSendStreamStats-devel

This package contains library source intended for building other packages which
use the "WebTransportSendStreamStats" feature of the "%{crate}" crate.

%package     -n %{name}+WebTransportStats-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebTransportStats-devel

This package contains library source intended for building other packages which
use the "WebTransportStats" feature of the "%{crate}" crate.

%package     -n %{name}+WebglColorBufferFloat-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebglColorBufferFloat-devel

This package contains library source intended for building other packages which
use the "WebglColorBufferFloat" feature of the "%{crate}" crate.

%package     -n %{name}+WebglCompressedTextureAstc-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebglCompressedTextureAstc-devel

This package contains library source intended for building other packages which
use the "WebglCompressedTextureAstc" feature of the "%{crate}" crate.

%package     -n %{name}+WebglCompressedTextureAtc-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebglCompressedTextureAtc-devel

This package contains library source intended for building other packages which
use the "WebglCompressedTextureAtc" feature of the "%{crate}" crate.

%package     -n %{name}+WebglCompressedTextureEtc-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebglCompressedTextureEtc-devel

This package contains library source intended for building other packages which
use the "WebglCompressedTextureEtc" feature of the "%{crate}" crate.

%package     -n %{name}+WebglCompressedTextureEtc1-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebglCompressedTextureEtc1-devel

This package contains library source intended for building other packages which
use the "WebglCompressedTextureEtc1" feature of the "%{crate}" crate.

%package     -n %{name}+WebglCompressedTexturePvrtc-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebglCompressedTexturePvrtc-devel

This package contains library source intended for building other packages which
use the "WebglCompressedTexturePvrtc" feature of the "%{crate}" crate.

%package     -n %{name}+WebglCompressedTextureS3tc-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebglCompressedTextureS3tc-devel

This package contains library source intended for building other packages which
use the "WebglCompressedTextureS3tc" feature of the "%{crate}" crate.

%package     -n %{name}+WebglCompressedTextureS3tcSrgb-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebglCompressedTextureS3tcSrgb-devel

This package contains library source intended for building other packages which
use the "WebglCompressedTextureS3tcSrgb" feature of the "%{crate}" crate.

%package     -n %{name}+WebglDebugRendererInfo-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebglDebugRendererInfo-devel

This package contains library source intended for building other packages which
use the "WebglDebugRendererInfo" feature of the "%{crate}" crate.

%package     -n %{name}+WebglDebugShaders-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebglDebugShaders-devel

This package contains library source intended for building other packages which
use the "WebglDebugShaders" feature of the "%{crate}" crate.

%package     -n %{name}+WebglDepthTexture-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebglDepthTexture-devel

This package contains library source intended for building other packages which
use the "WebglDepthTexture" feature of the "%{crate}" crate.

%package     -n %{name}+WebglDrawBuffers-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebglDrawBuffers-devel

This package contains library source intended for building other packages which
use the "WebglDrawBuffers" feature of the "%{crate}" crate.

%package     -n %{name}+WebglLoseContext-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebglLoseContext-devel

This package contains library source intended for building other packages which
use the "WebglLoseContext" feature of the "%{crate}" crate.

%package     -n %{name}+WebglMultiDraw-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WebglMultiDraw-devel

This package contains library source intended for building other packages which
use the "WebglMultiDraw" feature of the "%{crate}" crate.

%package     -n %{name}+WellKnownDirectory-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WellKnownDirectory-devel

This package contains library source intended for building other packages which
use the "WellKnownDirectory" feature of the "%{crate}" crate.

%package     -n %{name}+WgslLanguageFeatures-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WgslLanguageFeatures-devel

This package contains library source intended for building other packages which
use the "WgslLanguageFeatures" feature of the "%{crate}" crate.

%package     -n %{name}+WheelEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WheelEvent-devel

This package contains library source intended for building other packages which
use the "WheelEvent" feature of the "%{crate}" crate.

%package     -n %{name}+WheelEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WheelEventInit-devel

This package contains library source intended for building other packages which
use the "WheelEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+WidevineCdmManifest-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WidevineCdmManifest-devel

This package contains library source intended for building other packages which
use the "WidevineCdmManifest" feature of the "%{crate}" crate.

%package     -n %{name}+Window-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Window-devel

This package contains library source intended for building other packages which
use the "Window" feature of the "%{crate}" crate.

%package     -n %{name}+WindowClient-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WindowClient-devel

This package contains library source intended for building other packages which
use the "WindowClient" feature of the "%{crate}" crate.

%package     -n %{name}+Worker-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Worker-devel

This package contains library source intended for building other packages which
use the "Worker" feature of the "%{crate}" crate.

%package     -n %{name}+WorkerDebuggerGlobalScope-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WorkerDebuggerGlobalScope-devel

This package contains library source intended for building other packages which
use the "WorkerDebuggerGlobalScope" feature of the "%{crate}" crate.

%package     -n %{name}+WorkerGlobalScope-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WorkerGlobalScope-devel

This package contains library source intended for building other packages which
use the "WorkerGlobalScope" feature of the "%{crate}" crate.

%package     -n %{name}+WorkerLocation-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WorkerLocation-devel

This package contains library source intended for building other packages which
use the "WorkerLocation" feature of the "%{crate}" crate.

%package     -n %{name}+WorkerNavigator-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WorkerNavigator-devel

This package contains library source intended for building other packages which
use the "WorkerNavigator" feature of the "%{crate}" crate.

%package     -n %{name}+WorkerOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WorkerOptions-devel

This package contains library source intended for building other packages which
use the "WorkerOptions" feature of the "%{crate}" crate.

%package     -n %{name}+WorkerType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WorkerType-devel

This package contains library source intended for building other packages which
use the "WorkerType" feature of the "%{crate}" crate.

%package     -n %{name}+Worklet-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+Worklet-devel

This package contains library source intended for building other packages which
use the "Worklet" feature of the "%{crate}" crate.

%package     -n %{name}+WorkletGlobalScope-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WorkletGlobalScope-devel

This package contains library source intended for building other packages which
use the "WorkletGlobalScope" feature of the "%{crate}" crate.

%package     -n %{name}+WorkletOptions-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WorkletOptions-devel

This package contains library source intended for building other packages which
use the "WorkletOptions" feature of the "%{crate}" crate.

%package     -n %{name}+WritableStream-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WritableStream-devel

This package contains library source intended for building other packages which
use the "WritableStream" feature of the "%{crate}" crate.

%package     -n %{name}+WritableStreamDefaultController-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WritableStreamDefaultController-devel

This package contains library source intended for building other packages which
use the "WritableStreamDefaultController" feature of the "%{crate}" crate.

%package     -n %{name}+WritableStreamDefaultWriter-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WritableStreamDefaultWriter-devel

This package contains library source intended for building other packages which
use the "WritableStreamDefaultWriter" feature of the "%{crate}" crate.

%package     -n %{name}+WriteCommandType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WriteCommandType-devel

This package contains library source intended for building other packages which
use the "WriteCommandType" feature of the "%{crate}" crate.

%package     -n %{name}+WriteParams-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+WriteParams-devel

This package contains library source intended for building other packages which
use the "WriteParams" feature of the "%{crate}" crate.

%package     -n %{name}+XPathExpression-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XPathExpression-devel

This package contains library source intended for building other packages which
use the "XPathExpression" feature of the "%{crate}" crate.

%package     -n %{name}+XPathNsResolver-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XPathNsResolver-devel

This package contains library source intended for building other packages which
use the "XPathNsResolver" feature of the "%{crate}" crate.

%package     -n %{name}+XPathResult-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XPathResult-devel

This package contains library source intended for building other packages which
use the "XPathResult" feature of the "%{crate}" crate.

%package     -n %{name}+XmlDocument-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XmlDocument-devel

This package contains library source intended for building other packages which
use the "XmlDocument" feature of the "%{crate}" crate.

%package     -n %{name}+XmlHttpRequest-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XmlHttpRequest-devel

This package contains library source intended for building other packages which
use the "XmlHttpRequest" feature of the "%{crate}" crate.

%package     -n %{name}+XmlHttpRequestEventTarget-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XmlHttpRequestEventTarget-devel

This package contains library source intended for building other packages which
use the "XmlHttpRequestEventTarget" feature of the "%{crate}" crate.

%package     -n %{name}+XmlHttpRequestResponseType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XmlHttpRequestResponseType-devel

This package contains library source intended for building other packages which
use the "XmlHttpRequestResponseType" feature of the "%{crate}" crate.

%package     -n %{name}+XmlHttpRequestUpload-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XmlHttpRequestUpload-devel

This package contains library source intended for building other packages which
use the "XmlHttpRequestUpload" feature of the "%{crate}" crate.

%package     -n %{name}+XmlSerializer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XmlSerializer-devel

This package contains library source intended for building other packages which
use the "XmlSerializer" feature of the "%{crate}" crate.

%package     -n %{name}+XrBoundedReferenceSpace-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrBoundedReferenceSpace-devel

This package contains library source intended for building other packages which
use the "XrBoundedReferenceSpace" feature of the "%{crate}" crate.

%package     -n %{name}+XrEye-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrEye-devel

This package contains library source intended for building other packages which
use the "XrEye" feature of the "%{crate}" crate.

%package     -n %{name}+XrFrame-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrFrame-devel

This package contains library source intended for building other packages which
use the "XrFrame" feature of the "%{crate}" crate.

%package     -n %{name}+XrHand-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrHand-devel

This package contains library source intended for building other packages which
use the "XrHand" feature of the "%{crate}" crate.

%package     -n %{name}+XrHandJoint-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrHandJoint-devel

This package contains library source intended for building other packages which
use the "XrHandJoint" feature of the "%{crate}" crate.

%package     -n %{name}+XrHandedness-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrHandedness-devel

This package contains library source intended for building other packages which
use the "XrHandedness" feature of the "%{crate}" crate.

%package     -n %{name}+XrInputSource-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrInputSource-devel

This package contains library source intended for building other packages which
use the "XrInputSource" feature of the "%{crate}" crate.

%package     -n %{name}+XrInputSourceArray-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrInputSourceArray-devel

This package contains library source intended for building other packages which
use the "XrInputSourceArray" feature of the "%{crate}" crate.

%package     -n %{name}+XrInputSourceEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrInputSourceEvent-devel

This package contains library source intended for building other packages which
use the "XrInputSourceEvent" feature of the "%{crate}" crate.

%package     -n %{name}+XrInputSourceEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrInputSourceEventInit-devel

This package contains library source intended for building other packages which
use the "XrInputSourceEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+XrInputSourcesChangeEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrInputSourcesChangeEvent-devel

This package contains library source intended for building other packages which
use the "XrInputSourcesChangeEvent" feature of the "%{crate}" crate.

%package     -n %{name}+XrInputSourcesChangeEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrInputSourcesChangeEventInit-devel

This package contains library source intended for building other packages which
use the "XrInputSourcesChangeEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+XrJointPose-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrJointPose-devel

This package contains library source intended for building other packages which
use the "XrJointPose" feature of the "%{crate}" crate.

%package     -n %{name}+XrJointSpace-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrJointSpace-devel

This package contains library source intended for building other packages which
use the "XrJointSpace" feature of the "%{crate}" crate.

%package     -n %{name}+XrLayer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrLayer-devel

This package contains library source intended for building other packages which
use the "XrLayer" feature of the "%{crate}" crate.

%package     -n %{name}+XrPermissionDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrPermissionDescriptor-devel

This package contains library source intended for building other packages which
use the "XrPermissionDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+XrPermissionStatus-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrPermissionStatus-devel

This package contains library source intended for building other packages which
use the "XrPermissionStatus" feature of the "%{crate}" crate.

%package     -n %{name}+XrPose-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrPose-devel

This package contains library source intended for building other packages which
use the "XrPose" feature of the "%{crate}" crate.

%package     -n %{name}+XrReferenceSpace-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrReferenceSpace-devel

This package contains library source intended for building other packages which
use the "XrReferenceSpace" feature of the "%{crate}" crate.

%package     -n %{name}+XrReferenceSpaceEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrReferenceSpaceEvent-devel

This package contains library source intended for building other packages which
use the "XrReferenceSpaceEvent" feature of the "%{crate}" crate.

%package     -n %{name}+XrReferenceSpaceEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrReferenceSpaceEventInit-devel

This package contains library source intended for building other packages which
use the "XrReferenceSpaceEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+XrReferenceSpaceType-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrReferenceSpaceType-devel

This package contains library source intended for building other packages which
use the "XrReferenceSpaceType" feature of the "%{crate}" crate.

%package     -n %{name}+XrRenderState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrRenderState-devel

This package contains library source intended for building other packages which
use the "XrRenderState" feature of the "%{crate}" crate.

%package     -n %{name}+XrRenderStateInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrRenderStateInit-devel

This package contains library source intended for building other packages which
use the "XrRenderStateInit" feature of the "%{crate}" crate.

%package     -n %{name}+XrRigidTransform-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrRigidTransform-devel

This package contains library source intended for building other packages which
use the "XrRigidTransform" feature of the "%{crate}" crate.

%package     -n %{name}+XrSession-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrSession-devel

This package contains library source intended for building other packages which
use the "XrSession" feature of the "%{crate}" crate.

%package     -n %{name}+XrSessionEvent-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrSessionEvent-devel

This package contains library source intended for building other packages which
use the "XrSessionEvent" feature of the "%{crate}" crate.

%package     -n %{name}+XrSessionEventInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrSessionEventInit-devel

This package contains library source intended for building other packages which
use the "XrSessionEventInit" feature of the "%{crate}" crate.

%package     -n %{name}+XrSessionInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrSessionInit-devel

This package contains library source intended for building other packages which
use the "XrSessionInit" feature of the "%{crate}" crate.

%package     -n %{name}+XrSessionMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrSessionMode-devel

This package contains library source intended for building other packages which
use the "XrSessionMode" feature of the "%{crate}" crate.

%package     -n %{name}+XrSessionSupportedPermissionDescriptor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrSessionSupportedPermissionDescriptor-devel

This package contains library source intended for building other packages which
use the "XrSessionSupportedPermissionDescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+XrSpace-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrSpace-devel

This package contains library source intended for building other packages which
use the "XrSpace" feature of the "%{crate}" crate.

%package     -n %{name}+XrSystem-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrSystem-devel

This package contains library source intended for building other packages which
use the "XrSystem" feature of the "%{crate}" crate.

%package     -n %{name}+XrTargetRayMode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrTargetRayMode-devel

This package contains library source intended for building other packages which
use the "XrTargetRayMode" feature of the "%{crate}" crate.

%package     -n %{name}+XrView-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrView-devel

This package contains library source intended for building other packages which
use the "XrView" feature of the "%{crate}" crate.

%package     -n %{name}+XrViewerPose-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrViewerPose-devel

This package contains library source intended for building other packages which
use the "XrViewerPose" feature of the "%{crate}" crate.

%package     -n %{name}+XrViewport-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrViewport-devel

This package contains library source intended for building other packages which
use the "XrViewport" feature of the "%{crate}" crate.

%package     -n %{name}+XrVisibilityState-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrVisibilityState-devel

This package contains library source intended for building other packages which
use the "XrVisibilityState" feature of the "%{crate}" crate.

%package     -n %{name}+XrWebGlLayer-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrWebGlLayer-devel

This package contains library source intended for building other packages which
use the "XrWebGlLayer" feature of the "%{crate}" crate.

%package     -n %{name}+XrWebGlLayerInit-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XrWebGlLayerInit-devel

This package contains library source intended for building other packages which
use the "XrWebGlLayerInit" feature of the "%{crate}" crate.

%package     -n %{name}+XsltProcessor-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+XsltProcessor-devel

This package contains library source intended for building other packages which
use the "XsltProcessor" feature of the "%{crate}" crate.

%package     -n %{name}+console-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+console-devel

This package contains library source intended for building other packages which
use the "console" feature of the "%{crate}" crate.

%package     -n %{name}+css-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+css-devel

This package contains library source intended for building other packages which
use the "css" feature of the "%{crate}" crate.

%package     -n %{name}+gpu_buffer_usage-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+gpu_buffer_usage-devel

This package contains library source intended for building other packages which
use the "gpu_buffer_usage" feature of the "%{crate}" crate.

%package     -n %{name}+gpu_color_write-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+gpu_color_write-devel

This package contains library source intended for building other packages which
use the "gpu_color_write" feature of the "%{crate}" crate.

%package     -n %{name}+gpu_map_mode-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+gpu_map_mode-devel

This package contains library source intended for building other packages which
use the "gpu_map_mode" feature of the "%{crate}" crate.

%package     -n %{name}+gpu_shader_stage-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+gpu_shader_stage-devel

This package contains library source intended for building other packages which
use the "gpu_shader_stage" feature of the "%{crate}" crate.

%package     -n %{name}+gpu_texture_usage-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+gpu_texture_usage-devel

This package contains library source intended for building other packages which
use the "gpu_texture_usage" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-web-sys-devel -f %{oreon_filedir}/rust-web-sys-devel.list

%changelog

%autochangelog
